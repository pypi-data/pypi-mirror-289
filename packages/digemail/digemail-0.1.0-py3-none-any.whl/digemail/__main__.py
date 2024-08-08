import socketserver
from datetime import datetime
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from time import mktime
from typing import Annotated, Any, List, Literal, Optional, Union

import feedparser
import typer
from confz import BaseConfig, EnvSource, FileSource
from jinja2 import Template
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import (
    AnyHttpUrl,
    BaseModel,
    Field,
    FilePath,
    RootModel,
    SecretStr,
)
from pydantic.v1.types import SecretStr as SecretStrV1
from redmail.email.sender import EmailSender
from rich import print, print_json

feedparser.USER_AGENT = "digemail"


class EmailConfig(BaseConfig):
    subject: str = Field(default="digemail")
    host: str
    port: int
    username: str
    password: str
    sender: str
    receivers: List[str]


class RssConfig(BaseConfig):
    type: Literal["rss"]
    name: str
    link: AnyHttpUrl
    tags: List[str] = Field(default_factory=lambda: [])
    latest_n: int = Field(default=3)


class JsonConfig(BaseConfig):
    type: Literal["json"]
    name: str
    link: AnyHttpUrl
    tags: List[str] = []
    latest_n: int = 3


FeedConfig = Annotated[Union[RssConfig, JsonConfig], Field(discriminator="type")]


class AiConfig(BaseConfig):
    base_url: AnyHttpUrl
    api_key: SecretStr
    model: str
    temperature: float = Field(default=0.0)


class AiTransformConfig(BaseConfig):
    name: str
    type: Literal["ai"]
    prompt: str


class SortTransformConfig(BaseConfig):
    name: str
    type: Literal["sort"]
    reverse: bool = Field(default=True)


class DurationFilterTransformConfig(BaseConfig):
    name: str
    type: Literal["duration_filter"]
    duration: int = Field(default=60 * 60 * 24)


class TagFilterTransformConfig(BaseConfig):
    name: str
    type: Literal["tag_filter"]
    tags: List[str] = Field(default_factory=lambda: [])


class SelectTransformConfig(BaseConfig):
    name: str
    type: Literal["select"]
    start: int = Field(default=0)
    end: Optional[int] = Field(default=None)


TransformConfig = Annotated[
    Union[
        AiTransformConfig,
        SortTransformConfig,
        DurationFilterTransformConfig,
        TagFilterTransformConfig,
        SelectTransformConfig,
    ],
    Field(discriminator="type"),
]


class PipelineConfig(BaseConfig):
    name: str
    pipeline_tag: Optional[str] = Field(
        default=None,
        description=(
            "default tag `pipeline:{name}` will add to all entries in the pipeline"
        ),
    )
    transforms: List[str]


class Config(BaseConfig):
    template: FilePath = Field(default=Path("template.html"))
    ai: AiConfig
    email: EmailConfig
    feed: List[FeedConfig] = Field(default_factory=lambda: [])
    transform: List[TransformConfig] = Field(default_factory=lambda: [])
    pipeline: List[PipelineConfig] = Field(default_factory=lambda: [])

    CONFIG_SOURCES = [
        EnvSource(
            prefix="DM_", allow_all=True, file=".env.local", nested_separator="__"
        ),
        FileSource("config.toml"),
    ]


class Entry(BaseModel):
    link: str
    title: str
    time: datetime
    tag: List[str] = Field(default_factory=lambda: [])
    description: Optional[str] = Field(default=None)
    content: Optional[str] = Field(default=None)


def parse_rss(rss_config: RssConfig) -> List[Entry]:
    print(f"rss feed parsing {rss_config.name}")
    data = feedparser.parse(str(rss_config.link))

    def parse_entry(entry: Any):
        desc = content = None
        if hasattr(entry, "summary"):
            desc = entry.summary
        if hasattr(entry, "content") and len(entry.content) > 0:
            content = entry.content[0].value
        if hasattr(entry, "description"):
            desc = entry.description
        return Entry(
            link=entry.link,
            title=entry.title,
            time=datetime.fromtimestamp(mktime(entry.published_parsed)),
            tag=rss_config.tags,
            description=desc,
            content=content,
        )

    return [parse_entry(entry) for entry in data.entries]


def parse_feed(config: Config) -> List[Entry]:
    entries = []
    for feed in config.feed:
        if feed.type == "rss":
            entries.extend(parse_rss(feed))
        elif feed.type == "json":
            pass
    return entries


def ai_transform(
    ai_config: AiConfig, trans_config: AiTransformConfig, entries: List[Entry]
) -> List[Entry]:
    print(f"ai transform `{trans_config.name}` started")
    model = ChatOpenAI(
        base_url=str(ai_config.base_url),
        api_key=SecretStrV1(ai_config.api_key.get_secret_value()),
        model=ai_config.model,
        temperature=ai_config.temperature,
    )
    parser = JsonOutputParser(pydantic_object=RootModel[List[Entry]])
    prompt_template = PromptTemplate(
        template=trans_config.prompt + "\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt_template | model | parser

    result = []
    for entry in entries:
        try:
            output = chain.invoke({"query": f"[{entry.model_dump_json()}]"})
            entry_result = []
            assert isinstance(output, list)
            for output_entry in output:
                entry_result.append(
                    Entry(
                        link=output_entry["link"],
                        title=output_entry["title"],
                        time=output_entry["time"],
                        tag=output_entry["tag"],
                        description=output_entry["description"],
                        content=output_entry["content"],
                    )
                )
            result.extend(entry_result)
        except Exception as e:
            print(e)
            result.append(entry)
    return result


def sort_transform(
    sort_config: SortTransformConfig, entries: List[Entry]
) -> List[Entry]:
    print(f"sort transform `{sort_config.name}` started")
    return sorted(entries, key=lambda x: x.time, reverse=sort_config.reverse)


def duration_filter_transform(
    filter_config: DurationFilterTransformConfig, entries: List[Entry]
) -> List[Entry]:
    print(f"duration filter transform `{filter_config.name}` started")
    return [
        entry
        for entry in entries
        if (datetime.now() - entry.time).total_seconds() < filter_config.duration
    ]


def tag_filter_transform(
    filter_config: TagFilterTransformConfig, entries: List[Entry]
) -> List[Entry]:
    print(f"tag filter transform `{filter_config.name}` started")
    return [
        entry
        for entry in entries
        if all(tag in entry.tag for tag in filter_config.tags)
    ]


def select_transform(
    select_config: SelectTransformConfig, entries: List[Entry]
) -> List[Entry]:
    print(f"select transform `{select_config.name}` started")
    try:
        if select_config.end is None:
            result = entries[select_config.start :]
        result = entries[select_config.start : select_config.end]
    except Exception as e:
        print(f"select transform `{select_config.name}` error: {e}")
        result = entries
    return result


def get_transform_from_name(config: Config, name: str) -> TransformConfig:
    for transform in config.transform:
        if transform.name == name:
            return transform
    raise ValueError(f"transform {name} not found")


def transform_single_pipeline(
    config: Config, pipeline_config: PipelineConfig, entries: List[Entry]
) -> List[Entry]:
    print(f"pipeline `{pipeline_config.name}` started")
    try:
        for name in pipeline_config.transforms:
            transform = get_transform_from_name(config, name)
            if transform.type == "ai":
                entries = ai_transform(config.ai, transform, entries)
            elif transform.type == "sort":
                entries = sort_transform(transform, entries)
            elif transform.type == "duration_filter":
                entries = duration_filter_transform(transform, entries)
            elif transform.type == "tag_filter":
                entries = tag_filter_transform(transform, entries)
            elif transform.type == "select":
                entries = select_transform(transform, entries)
            else:
                raise ValueError(
                    f"unknown transform type {transform.type} "
                    f"for transform {transform.name}"
                )
    except Exception as e:
        print(f"pipeline `{pipeline_config.name}` error: {e}")
    return entries


def transform_pipeline(config: Config, entries: List[Entry]) -> List[Entry]:
    result = []
    for pipeline in config.pipeline:
        result.extend(transform_single_pipeline(config, pipeline, entries))
    return result


def render_html(config: Config, entries: List[Entry]) -> str:
    template = Template(config.template.read_text())
    return template.render(entries=entries)


def send_email(email_config: EmailConfig, html: str):
    email = EmailSender(
        host=email_config.host,
        port=email_config.port,
        username=email_config.username,
        password=email_config.password,
    )
    email.send(
        subject=email_config.subject,
        html=html,
        sender=email_config.sender,
        receivers=email_config.receivers,
    )


app = typer.Typer()


@app.command(name="config")
def config():
    config = Config()
    print_json(config.model_dump_json())


@app.command(name="entry")
def entry():
    config = Config()
    entries = parse_feed(config)
    transformed = transform_pipeline(config, entries)
    for entry in transformed:
        print(f"{entry.time} {entry.title} {entry.link}")


@app.command(name="preview")
def preview(port: int = 8080):
    config = Config()
    entries = parse_feed(config)
    transformed = transform_pipeline(config, entries)
    html = render_html(config, transformed)

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

    with socketserver.TCPServer(("", port), MyHandler) as httpd:
        print(f"Preview server started at http://localhost:{port}")
        httpd.serve_forever()


@app.command(name="send")
def send():
    config = Config()
    entries = parse_feed(config)
    transformed = transform_pipeline(config, entries)
    html = render_html(config, transformed)
    send_email(config.email, html)


if __name__ == "__main__":
    app()
