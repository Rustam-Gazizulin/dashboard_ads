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


@pytest.mark.django_db
def test_list_ads(api_client):

    url = reverse('ads_list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_ads(api_client, ads):

    expected_response = {
        "id": ads.pk,
        "author_id": ads.author_id,
        "image": None,
        "name": ads.name,
        "price": ads.price,
        "description": None,
        "is_published": False,
        "author": str(ads.author.username),
    }

    url = reverse('ads_retrieve', kwargs={"pk": ads.pk})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
