import requests
import pytest
import os

from alectio.client import AlectioClient
from alectio.exceptions import APIKeyNotFound

# one with enviroment variable and one with
def test_with_out_env():
    _environ = os.environ
    if "ALECTIO_API_KEY" in _environ:
        del os.environ['ALECTIO_API_KEY']
    with pytest.raises(APIKeyNotFound):
        aletio_client = AlectioClient()
        assert aletio_client == APIKeyNotFound
