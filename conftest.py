import allure
import pytest
import requests

from data import DataIngredients
from helpers import generate_email, generate_password, generate_username
from faker import Faker
from urls import Urls

faker = Faker()


@pytest.fixture
def generate_data():
    email = generate_email()
    password = generate_password()
    name = generate_username()
    return email, password, name


@allure.step("Создание и удаление пользователя")
@pytest.fixture
def create_and_delete_user(generate_data):
    email, password, name = generate_data
    params = {
        "email": email,
        "password": password,
        "name": name,
    }
    response = requests.post(
        f"{Urls.BASE}{Urls.CREATE_USER}",
        json=params,
    )
    data = response.json()
    user_data = [email, password, name]

    yield user_data, response.json()

    auth_token = data.get("accessToken")
    headers = {
        "Authorization": f"{auth_token}",
    }
    requests.delete(f"{Urls.BASE}{Urls.DELETE_USER}", headers=headers)


@allure.step("Создание заказа")
@pytest.fixture
def create_order(create_and_delete_user):
    access_token = create_and_delete_user[1]["accessToken"]
    payload = DataIngredients.PAILOAD
    headers = {"Authorization": f"{access_token}"}
    response = requests.post(
        f"{Urls.BASE}{Urls.CREATE_ORDER}",
        json=payload,
        headers=headers,
    )
    data = response.json()
    return data
