import allure
import requests

from data import DataMessage, DataIngredients
from urls import Urls


class TestCreateOrder:
    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("При заказе передаются ингредиенты")
    def test_create_order_auth_user_with_ingredients(self, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {
            "Authorization": f"{auth_token}",
        }
        payload = DataIngredients.PAILOAD
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_ORDER}",
            data=payload,
            headers=headers,
        )
        data = response.json()

        assert response.status_code == 200 and data["success"]

    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("Не передаются ингредиенты")
    def test_create_order_auth_user_without_ingredients(self, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {
            "Authorization": f"{auth_token}",
        }
        payload = {
            "ingredients": [""],
        }
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_ORDER}",
            data=payload,
            headers=headers,
        )
        data = response.json()

        assert response.status_code == 400 and not data["success"]

    @allure.title("Создание заказа неавторизованным пользователем")
    @allure.description("Передаются существующие ингредиенты")
    def test_create_order_unauth_user_with_ingredients(self):
        payload = DataIngredients.PAILOAD
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_ORDER}",
            data=payload,
        )
        data = response.json()

        assert response.status_code == 200 and data["success"]

    @allure.title("Создание заказа неавторизованным пользователем")
    @allure.description("Не передаются ингредиенты")
    def test_create_order_unauth_user_withot_ingredients(self):
        payload = {
            "ingredients": [""],
        }
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_ORDER}",
            data=payload,
        )
        data = response.json()

        assert response.status_code == 400 and not data["success"]

    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("Передаются ингредиенты с неверным хешем")
    def test_create_order_auth_user_with_wrong_hash(self, create_and_delete_user):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {"Authorization": f"{auth_token}"}
        payload = DataIngredients.INVALID_PAYLOAD
        response = requests.post(
            f"{Urls.BASE}{Urls.CREATE_ORDER}",
            data=payload,
            headers=headers,
        )

        # В документации ожидается код ответа 500 почему-то, а в реальности сервер возвращет 400.
        # Я проконсультровалась с наставником и он сказал проверять на код ответа как он описан в
        # документации (даже если он очень странный - 500 - это ошибка сервера, а не запроса).
        # Поэтому:
        # (a) этот тест фейлится
        # (b) проверяется на 500
        assert response.status_code == 500 and response.json() == DataMessage.MES_ONE_OR_MORE_IDS_PROVIDED_INCORRECT
