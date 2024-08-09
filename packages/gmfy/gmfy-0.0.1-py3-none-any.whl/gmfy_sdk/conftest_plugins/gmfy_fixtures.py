import pytest
import requests_mock

from gmfy_sdk.sdk import GMFYSDK
from settings import GMFY_API_KEY, GMFY_URL


@pytest.fixture()
def gmfy():
    return GMFYSDK(api_key=GMFY_API_KEY, base_url=GMFY_URL)


@pytest.fixture()
def gmfy_mock():
    with requests_mock.Mocker() as mock:
        yield mock
