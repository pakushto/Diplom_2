import pytest
import allure
from api.user_api import UserApi
from data import UserData


class TestPatchUser:
    @pytest.mark.parametrize("param,new_value", [
    ("email", "test123@greathouse.ru"),
    ("name", "new_name_123")
    ])
    @allure.title("Обновление {param} пользователя проходит успешно")
    @allure.description("Проверяем успешное обновление параметра {param} у пользователя")
    def test_patch_user_success(self, param, new_value, create_user):
        body = {param: new_value}
        response = UserApi.patch_user(body, create_user["access_token"])

        assert response.status_code == 200, f'Ожидался статус код 200, а вернулся {response.status_code}'
        assert response.json().get("success") == True, f'Ожидалось в теле запроса "success": true, а вернулось {response.json().get("success")}'

    @allure.title("Обновление неавторизированного пользователя возвращает ошибку 401")
    @allure.description("Проверяем, что при попытке обновления пользователя без токена авторизации возвращается ошибка 401 и корректное сообщение об ошибке")
    def test_path_unauthorized_user_returns_error_401(self, create_user):
        response = UserApi.patch_user(UserData.PATCH_USER_BODY)

        assert response.status_code == 401, f'Ожидался статус код 401, а вернулся {response.status_code}'
        assert response.json() == UserData.PATCH_USER_UNAUTHORIZED_RESPONSE, f'Ожидалcя ответ {UserData.PATCH_USER_UNAUTHORIZED_RESPONSE}, а вернулся {response.json()}'