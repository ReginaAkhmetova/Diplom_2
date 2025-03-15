import allure
import pytest
import requests

from data import DataMessage
from urls import Urls
from helpers import generate_username, generate_email, generate_password


class TestCreateUser:
    @allure.title("Успешное создание уникального пользователя")
    @allure.description("Передаются все обязательные поля")
    def test_create_user(self):
        payload = {
            "email": generate_email(),
            "password": generate_password(),
            "name": generate_username(),
        }
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_USER}",
            json=payload,
        )
        data = response.json()
        assert response.status_code == 200 and data["success"]

    @allure.title("Проверка создания уже зарегистрированного пользователя")
    @allure.description("Передаются поля уже созданного пользователя")
    def test_not_create_same_user(self):
        payload = {
            "email": "polosatik@ya.ru",
            "password": "qwerty1",
            "name": "polosatik",
        }
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_USER}",
            json=payload,
        )
        assert response.status_code == 403 and response.json() == DataMessage.MES_USER_EXIST

    @allure.title("Получение ошибки при создании пользователя без одного из обязательных полей")
    @allure.description("По очереди не передается одно из обязательных полей")
    @pytest.mark.parametrize(
        "params",
        [
            {  # пустое значение имени
                "email": generate_email(),
                "password": generate_email(),
                "name": "",
            },
            {  # пустое значение email
                "email": "",
                "password": generate_password(),
                "name": generate_password(),
            },
            {  # пустое значение пароля
                "email": generate_username(),
                "password": "",
                "name": generate_username(),
            },
        ],
    )
    def test_create_user_without_one_required_fields(self, params):
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_USER}",
            json=params,
        )
        assert response.status_code == 403 and response.json() == DataMessage.MES_NO_ONE_OF_THE_FIELDS
