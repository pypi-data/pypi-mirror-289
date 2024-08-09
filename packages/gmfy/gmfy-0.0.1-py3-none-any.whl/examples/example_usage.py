from gmfy_sdk.constants import BaseEventAction, BaseEventType
from gmfy_sdk.sdk import GMFYSDK
from settings import GMFY_API_KEY, GMFY_URL


class EventType(BaseEventType):
    subscription = "subscription"
    subscriber = "subscriber"


class EventAction(BaseEventAction):
    create = "create"
    remove = "remove"


def main():
    gmfy_sdk = GMFYSDK(GMFY_API_KEY, GMFY_URL)
    data = [
        {
            "event_type": EventType.subscription,
            "user_id": "12345",
            "event_action": EventAction.create,
        },
        {
            "event_type": EventType.subscriber,
            "user_id": "54321",
            "event_action": EventAction.create,
        },
    ]
    gmfy_sdk.create_batch_events(data)


if __name__ == "__main__":
    main()
