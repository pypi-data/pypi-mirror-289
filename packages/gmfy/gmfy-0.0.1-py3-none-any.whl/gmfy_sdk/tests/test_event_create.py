from examples.example_usage import EventAction, EventType
from settings import GMFY_URL


def test_send_gmfy_subscription_create(gmfy_mock, gmfy):
    gmfy_mock.post(
        f"{GMFY_URL}v1/events/batch/",
        status_code=201,
    )
    gmfy.create_batch_events(
        [
            {
                "event_type": EventType.subscription,
                "user_id": "12345",
                "event_action": EventAction.create,
            },
        ],
    )

    assert gmfy_mock.called
    assert gmfy_mock.last_request.json() == [
        {
            "userId": "12345",
            "eventType": "subscription",
            "type": "create_subscription",
        },
    ]


def test_send_gmfy_subscription_remove(gmfy_mock, gmfy):
    gmfy_mock.post(
        f"{GMFY_URL}v1/events/batch/",
        status_code=201,
    )
    gmfy.create_batch_events(
        [
            {
                "event_type": EventType.subscription,
                "user_id": "12345",
                "event_action": EventAction.remove,
            },
        ],
    )

    assert gmfy_mock.called
    assert gmfy_mock.last_request.json() == [
        {
            "userId": "12345",
            "eventType": "subscription",
            "type": "remove_subscription",
        },
    ]
