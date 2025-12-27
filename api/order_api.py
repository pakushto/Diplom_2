import requests
import allure
from urls import Urls

class OrderApi:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body, access_token=None):
        headers = {
            "Authorization": access_token
        }
        return requests.post(Urls.CREATE_ORDER_URL, headers=headers, json=body)
    
    @staticmethod
    @allure.step("Получение списка заказов пользователя")
    def get_user_orders(access_token=None):
        headers = {
            "Authorization": access_token
        }
        return requests.get(Urls.GET_USER_ORDERS, headers=headers)
