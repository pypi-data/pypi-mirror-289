from dataclasses import dataclass

from wscli.api_utils.api_endpoint import ApiEndpoint
from wscli.api_utils.call_config import Scheme


@dataclass(kw_only=True)
class ApiUrl:
    domain: str = "localhost"
    scheme: Scheme = Scheme.HTTP
    port: int = 8000
    base_route: str = ""

    def url(self, endpoint: str | ApiEndpoint = ""):
        base_route = self.base_route.strip("/")
        route = f"{base_route}/{str(endpoint).strip('/')}"
        return f"{self.scheme.value}://{self.domain}:{self.port}/{route}"
