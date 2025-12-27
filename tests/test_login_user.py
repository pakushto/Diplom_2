import pytest
import allure
from api.user_api import UserApi
from helper import ChangeTestDataHelper
from data import UserData


class TestLoginUser:
    @allure.title("Авторизация пользователя проходит успешно")
    @allure.description("Проверяем успешную авторизацию пользователя с валидными данными")
    def test_login_user_succes(self, create_user):
        response = UserApi.login_user(create_user["login_body"])

        assert response.status_code == 200, f'Ожидался статус код 200, а вернулся {response.status_code}'
        assert response.json().get("success") == True, f'Ожидалось в теле запроса "success": true, а вернулось {response.json().get("success")}'

    @pytest.mark.parametrize("param", [
        pytest.param("email"),
        pytest.param("password")
    ])
    @allure.title("Авторизация пользователя с неверным {parameter} возвращает ошибку 403")
    @allure.description("Проверяем, что при попытке авторизации пользователя с некорректным параметром в теле запроса возвращается ошибка 401 и корректное сообщение об ошибке")
    def test_login_user_with_incorrect_param_returns_error_401(self, param, create_user):
        body = create_user["login_body"]
        response = UserApi.login_user(ChangeTestDataHelper.modify_param_from_body(body=body,key=param, value="Incorrect"))

        assert response.status_code == 401, f'Ожидался статус код 401, а вернулся {response.status_code}'
        assert response.json() == UserData.LOGIN_USER_INCORRECT_PARAMS_RESPONSE, f'Ожидалcя ответ {UserData.LOGIN_USER_INCORRECT_PARAMS_RESPONSE}, а вернулся {response.json()}'