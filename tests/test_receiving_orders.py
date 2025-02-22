import allure
import requests
from urls import Urls


class TestReceivingOrders:
    @allure.title("Получение заказа авторизованного пользователя")
    @allure.description("Передается токен пользователя")
    def test_receiving_orders_auth_user(self, create_and_delete_user, create_order):
        auth_token = create_and_delete_user[1]["accessToken"]
        headers = {
            "Authorization": f"{auth_token}",
        }
        response = requests.get(f"{Urls.BASE}{Urls.RECEIVING_ORDERS}", headers=headers)
        data = response.json()
        assert response.status_code == 200 and data["success"] and "orders" in data

    @allure.title("Получение заказа авторизованного пользователя")
    @allure.description("Передается токен пользователя")
    def test_receiving_orders_unauth_user(self):
        response = requests.get(f"{Urls.BASE}{Urls.RECEIVING_ORDERS}")
        data = response.json()
        assert response.status_code == 401 and not data["success"]
