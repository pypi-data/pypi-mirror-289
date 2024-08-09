from __future__ import annotations

from functools import reduce
from operator import or_
from typing import TypeAlias

from pydantic import Field, RootModel

from gmfy_sdk.events.base_events import Event

Events: TypeAlias = reduce(or_, Event.model_config["children_list"])  # type: ignore[typeddict-item, valid-type]


class EventManager(RootModel):
    root: list[Events] = Field(discriminator="event_type")
