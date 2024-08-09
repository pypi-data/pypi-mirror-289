import logging
from typing import Any

import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout

from gmfy_sdk.events import EventManager

logger = logging.getLogger(__name__)


class GMFYApiClient:
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def _post(self, url: str, data: Any) -> None:
        headers = {
            "x-api-key": self.token,
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(
                url=url,
                data=data,
                headers=headers,
                timeout=60,
                verify=False,  # noqa: S501
            )
            response.raise_for_status()
        except HTTPError:
            logger.exception("Bad response status")
        except (ConnectionError, Timeout, RequestException):
            logger.exception("Error fetching gmfy")

    def create_events(self, event_manager: EventManager) -> None:
        url = f"{self.url}v1/events/batch/"
        dumped_events = event_manager.model_dump_json(by_alias=True)
        self._post(url, dumped_events)
