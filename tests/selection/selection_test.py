import json

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_selection(api_client, user, ads):
    data = {
        "name": 'testnewselection',
        "owner": user.id,
        "items": [ads.id]
    }

    url = reverse('selection_create')
    response = api_client.post(
        url,
        data=json.dumps(data),
        content_type='application/json',
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == data["name"]
    assert response.data["owner"] == data["owner"]
