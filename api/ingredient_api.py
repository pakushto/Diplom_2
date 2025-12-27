import requests
import allure
from urls import Urls

class IngredientApi:
    @staticmethod
    @allure.step("Получение списка ингридиентов")
    def get_ingedients():
        return requests.get(Urls.GET_INGREDIENTS_URL)