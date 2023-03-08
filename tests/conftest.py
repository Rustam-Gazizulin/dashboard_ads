import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import SelectionFactory, UserFactory, AdsFactory

register(SelectionFactory)
register(UserFactory)
register(AdsFactory)


@pytest.fixture
def api_client(db, user):
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client
