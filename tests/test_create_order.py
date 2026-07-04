import allure
from api.order_api import OrderApi
from helper import OrderFactory
from data import OrderData

class TestCreateOrder:
    @allure.title("Создание заказа проходит успешно")
    @allure.description("Проверяем успешное создание заказа с валидными данными")
    def test_create_order_success(self, ingredient_list, create_user):
        body = OrderFactory.order_body_with_ingredients(ingredient_list)
        response = OrderApi.create_order(body, create_user["access_token"])

        assert response.status_code == 200, f'Ожидался статус код 200, а вернулся {response.status_code}'
        assert response.json().get("success") == True, f'Ожидалось в теле запроса "success": true, а вернулось {response.json().get("success")}'

    @allure.title("Создание заказа без авторизации проходит успешно")
    @allure.description("Проверяем успешное создание заказа без токена авторизации")
    def test_create_order_without_auth_success(self, ingredient_list, create_user):
        body = OrderFactory.order_body_with_ingredients(ingredient_list)
        response = OrderApi.create_order(body)

        assert response.status_code == 200, f'Ожидался статус код 200, а вернулся {response.status_code}'
        assert response.json().get("success") == True, f'Ожидалось в теле запроса "success": true, а вернулось {response.json().get("success")}'        

    @allure.title("Создание заказа без ингредиентов возвращает ошибку 400")
    @allure.description("Проверяем, что при попытке создать заказ без ингредиентов возвращается ошибка 401 и корретное сообщение об ошибке")
    def test_create_order_without_ingredients_returns_error_400(self):
        body = OrderFactory.order_body_without_ingredients()
        response = OrderApi.create_order(body)

        assert response.status_code == 400, f'Ожидался статус код 400, а вернулся {response.status_code}'
        assert response.json() == OrderData.CREATE_ORDER_WITHOUT_INGREDIENTS_RESPONSE, f'Ожидалcя ответ {OrderData.CREATE_ORDER_WITHOUT_INGREDIENTS_RESPONSE}, а вернулся {response.json()}'

    @allure.title("Создание заказа с некорректным ингредиентом возвращает ошибку 500")
    @allure.description("Проверяем, что при попытке создать заказ с некорректным id ингредиента возвращается ошибка 500")
    def test_create_order_with_incorrect_ingerdient_returns_error_500(self):
        body = OrderFactory.order_body_with_incorrect_ingredient()
        response = OrderApi.create_order(body)

        assert response.status_code == 500, f'Ожидался статус код 500, а вернулся {response.status_code}'
