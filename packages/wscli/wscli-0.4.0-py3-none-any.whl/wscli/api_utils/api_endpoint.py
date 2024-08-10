from dataclasses import dataclass
from typing import Any


@dataclass
class ApiEndpoint:
    resource: str = ""
    id: Any | None = None
    subresource: str = ""

    def __str__(self):
        if not self.resource or self.resource == "/":
            return self.resource
        endpoint = self.resource
        if self.id is not None:
            endpoint = endpoint + f"/{self.id}"
        if self.subresource:
            endpoint = endpoint + f"/{self.subresource}"
        return endpoint
