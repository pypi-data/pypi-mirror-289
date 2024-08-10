from dataclasses import dataclass
from enum import Enum
from typing import Dict

from wscli.api_utils import ApiEndpoint


class Scheme(Enum):
    HTTP = "http"
    HTTPS = "https"


class Method(Enum):
    GET = "get"
    POST = "post"


class ContentType(Enum):
    HTML = "text/html"
    JSON = "application/json"


@dataclass(kw_only=True)
class CallConfig:
    token: str | None = None
    method: Method = Method.GET
    content_type: ContentType | None = None
    endpoint: ApiEndpoint | None = None

    @classmethod
    def api_post(
        cls, token: str | None = None, endpoint: ApiEndpoint | None = None
    ):
        return cls(
            token=token,
            method=Method.POST,
            content_type=ContentType.JSON,
            endpoint=endpoint,
        )

    @classmethod
    def api_get(
        cls, token: str | None = None, endpoint: ApiEndpoint | None = None
    ):
        return cls(
            token=token,
            endpoint=endpoint,
            method=Method.GET,
            content_type=ContentType.JSON,
        )

    @property
    def headers(self) -> Dict[str, str]:
        headers: Dict[str, str] = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if self.content_type:
            headers["Content-type"] = str(self.content_type.value)
        return headers
