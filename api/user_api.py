import requests
import allure
from urls import Urls


class UserApi:
    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(body: dict):
        return requests.post(Urls.CREATE_USER_URL, json=body)
    
    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token: str):
        headers = {
            "Authorization": access_token
        }
        
        return requests.delete(Urls.DELETE_USER_URL, headers=headers)
    
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(body: dict):
        return requests.post(Urls.LOGIN_USER_URL, json=body)
    
    @staticmethod
    @allure.step("Обновление пользователя")
    def patch_user(body: dict, access_token=None):
        headers = {
            "Authorization": access_token
        }
        return requests.patch(Urls.PATCH_USER_URL, headers=headers, json=body)