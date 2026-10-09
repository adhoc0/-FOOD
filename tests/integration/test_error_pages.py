import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_404_uses_custom_template(client):
    response = client.get("/olmayan-sayfa/")
    assert response.status_code == 404
    assert "Aradığınız sayfa bulunamadı" in response.content.decode()


@pytest.mark.django_db
def test_robots_txt(client):
    response = client.get(reverse("robots_txt"))
    assert response.status_code == 200
    assert response["Content-Type"].startswith("text/plain")
    body = response.content.decode()
    assert "User-agent: *" in body
    assert "/sitemap.xml" in body


def test_500_template_renders():
    from django.template.loader import render_to_string

    assert "Bir şeyler ters gitti" in render_to_string("500.html")
