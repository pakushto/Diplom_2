import allure
from api.order_api import OrderApi
from data import OrderData

class TestGetUserOrders:
    @allure.title("Получение заказов пользователя проходит успешно")
    @allure.description("Проверяем успешное получение заказов пользователя")
    def test_get_user_orders_succes(self, create_user_order):
        response = OrderApi.get_user_orders(create_user_order["access_token"])

        assert response.status_code == 200, f'Ожидался статус код 200, а вернулся {response.status_code}'
        assert response.json().get("success") == True, f'Ожидалось в теле запроса "success": true, а вернулось {response.json().get("success")}'
        assert response.json().get("orders"), f'Ожидался непустой список orders, а вернулся пустой {response.json().get("orders")}' 

    @allure.title("Получение заказов неавторизированного пользователя возвращает ошибку 401")
    @allure.description("Проверяем, что при попытке получения заказов пользователя без токена авторизации возвращается ошибка 401 и корректное сообщение об ошибке")
    def test_get_user_orders_without_auth_returns_error_401(self):
        response = OrderApi.get_user_orders()

        assert response.status_code == 401, f'Ожидался статус код 401, а вернулся {response.status_code}'
        assert response.json() == OrderData.GET_USER_ORDERS_WITHOUT_AUTH_RESPONSE, f'Ожидалcя ответ {OrderData.GET_USER_ORDERS_WITHOUT_AUTH_RESPONSE}, а вернулся {response.json()}'