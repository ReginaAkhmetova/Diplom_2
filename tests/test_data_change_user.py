import allure
import pytest
import requests

from data import DataMessage
from helpers import generate_username, generate_email, generate_password
from urls import Urls


class TestChangeUserData:
    @allure.title("Изменение данных авторизованного пользователя")
    @allure.description("Передается каждое из полей")
    @pytest.mark.parametrize(
        "new_data",
        [
            ({"email": generate_email()}),
            ({"password": generate_password()}),
            ({"name": generate_username()}),
        ],
    )
    def test_data_change_auth_user(self, new_data, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {"Authorization": f"{auth_token}"}
        payload = new_data
        response = requests.patch(
            f"{Urls.BASE}{Urls.DATA_CHANGE_USER}",
            json=payload,
            headers=headers,
        )
        data = response.json()
        assert response.status_code == 200 and data["success"]

    @allure.title("Проверка изменения данных неавторизованного пользователя")
    @allure.description("передается каждое из полей")
    @pytest.mark.parametrize(
        "new_data",
        [
            ({"email": generate_email()}),
            ({"password": generate_password()}),
            ({"name": generate_username()}),
        ],
    )
    def test_data_change_unauth_user(self, new_data):
        payload = new_data
        response = requests.patch(
            f"{Urls.BASE}{Urls.DATA_CHANGE_USER}",
            json=payload,
        )
        data = response.json()

        assert response.status_code == 401 and data == DataMessage.MES_YOU_SHOULD_BE_AUTHORISED
