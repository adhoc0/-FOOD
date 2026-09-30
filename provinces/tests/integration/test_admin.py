"""Province ve Region admin entegrasyon testleri."""

import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import AdminFactory, ProvinceFactory, RegionFactory, UserFactory


@pytest.fixture
def admin_client():
    client = Client()
    client.force_login(AdminFactory())
    return client


@pytest.mark.django_db
@pytest.mark.parametrize("model_name", ["province", "region"])
def test_changelist_loads_for_superuser(admin_client, model_name):
    ProvinceFactory()

    response = admin_client.get(reverse(f"admin:provinces_{model_name}_changelist"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_province_change_page_loads(admin_client):
    province = ProvinceFactory()

    response = admin_client.get(
        reverse("admin:provinces_province_change", args=[province.pk])
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_region_change_page_loads(admin_client):
    region = RegionFactory()

    response = admin_client.get(
        reverse("admin:provinces_region_change", args=[region.pk])
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_regular_user_cannot_access_admin():
    client = Client()
    client.force_login(UserFactory())

    response = client.get(reverse("admin:provinces_province_changelist"))

    assert response.status_code == 302
    assert "login" in response["Location"]
