import logging

import requests

from wscli.api_utils.api_endpoint import ApiEndpoint
from wscli.api_utils.api_url import ApiUrl
from wscli.api_utils.call_config import CallConfig

logger = logging.getLogger(__name__)


def hit_api(
    api_url: ApiUrl,
    call_config: CallConfig | None = None,
    endpoint: ApiEndpoint | str | None = None,
    payload: dict | None = None,
) -> requests.Response:
    if isinstance(endpoint, str):
        endpoint = ApiEndpoint(resource=endpoint)
    call_config = call_config or CallConfig()
    endpoint = endpoint or call_config.endpoint or ApiEndpoint()
    url = api_url.url(str(endpoint))
    method = call_config.method.value

    logger.warning(
        f"making request {call_config.method.name} to endpoint {url}"
    )
    response = requests.request(
        method, url, headers=call_config.headers, json=payload
    )
    return response
