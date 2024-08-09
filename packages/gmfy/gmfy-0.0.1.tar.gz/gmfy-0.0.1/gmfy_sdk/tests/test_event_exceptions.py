import requests

from examples.example_usage import EventAction, EventType
from settings import GMFY_URL


def test_gmfy_sdk_validation_error(gmfy, caplog):
    gmfy.create_batch_events(
        [
            {
                "event_type": 5,
                "user_id": "1",
            },
        ],
    )
    assert "Validation error when creating event" in caplog.text


def test_gmfy_api_client_http_error(gmfy, gmfy_mock, caplog):
    gmfy_mock.request(
        url=f"{GMFY_URL}v1/events/batch/",
        method="post",
        exc=requests.HTTPError,
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
    assert "Bad response status" in caplog.text


def test_gmfy_api_client_other_error(gmfy, gmfy_mock, caplog):
    gmfy_mock.request(
        url=f"{GMFY_URL}v1/events/batch/",
        method="post",
        exc=requests.Timeout,
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
    assert "Error fetching gmfy" in caplog.text
