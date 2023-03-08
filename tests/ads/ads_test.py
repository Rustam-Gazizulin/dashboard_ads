import json

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_ads(api_client, user):

    expected_response = {
        "id": 1,
        "image": None,
        "name": "test ads new",
        "price": 100,
        "description": None,
        "is_published": False,
        "author": 1,
        "category": None
    }

    data = {
        "name": "test ads new",
        "author": user.id,
        "price": 100,
    }

    url = reverse('ads_create')
    response = api_client.post(
        url,
        data=json.dumps(data),
        content_type='application/json',
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response


