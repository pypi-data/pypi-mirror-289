import logging
from typing import Any, Dict, List

from pydantic import ValidationError

from gmfy_sdk.events import EventManager
from gmfy_sdk.gmfy_api_client import GMFYApiClient

logger = logging.getLogger(__name__)


class GMFYSDK:
    def __init__(self, api_key: str, base_url: str):
        self.api_client = GMFYApiClient(api_key, base_url)

    def create_batch_events(self, events: List[Dict[str, Any]]) -> None:  # noqa: FA100
        """
        Creates a batch of events and sends them to GMFY.
        """
        try:
            event_manager = EventManager(events)
            self.api_client.create_events(event_manager)
        except ValidationError:
            logger.exception("Validation error when creating event batch")
            return
        except Exception:
            logger.exception("Unexpected error when creating event batch")
            return
