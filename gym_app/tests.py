from django.test import TestCase, Client
import pytest
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_example_view():
    c = Client()
    response = c.get("/trainings/")
    assert response.status_code == 200
    assert "Trainings list" in str(response.content, "utf-8")


@pytest.mark.django_db
def test_add_user():
    c = Client()
    response = c.get("/add_user/")
    assert response.status_code == 200
    response2 = c.post(
        "/add_user/",
        {
            "user": "andrzejek",
            "password_1": "Endriu223!",
            "password_2": "Endriu223!",
            "first_name": "Andrzej",
            "last_name": "Bengalski",
            "email": "endriu@o2.com",
        },
        follow=True,
    )

    assert response2.status_code == 200


@pytest.mark.django_db
def test_add_breeding():
    u = User.objects.create_user(username="Tosia", password="Tosia123!")
    c = Client()
    c.login(username="Tosia", password="Tosia123!")
    response = c.post(
        "/members/",
    )
    assert response.status_code == 403
