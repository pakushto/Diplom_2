import pytest
import allure
from api.user_api import UserApi
from helper import UserFactory, ChangeTestDataHelper
from data import UserData


class TestCreateUser:
    @allure.title("Создание пользователя проходит успешно")
    @allure.description("Проверяем успешное создание пользователя с валидными данными")
    def test_create_user_success(self, cleanup_user):
        response = UserApi.create_user(UserFactory.default_body_with_random_params())
        cleanup_user.append(response.json()["accessToken"])

        assert response.status_code == 200, f'Ожидался статус код 200, а вернулся {response.status_code}'
        assert response.json().get("success") == True, f'Ожидалось в теле запроса "success": true, а вернулось {response.json().get("success")}'

    @allure.title("Создание уже существующего пользователя возвращает ошибку 403")
    @allure.description("Проверяем, что при повторной попытке создать пользователя с той же почтой возвращается 403")
    def test_create_duplicate_user_returns_error_403(self, create_user):
        response = UserApi.create_user(create_user["body"])

        assert response.status_code == 403, f'Ожидался статус код 403, а вернулся {response.status_code}'
        assert response.json() == UserData.CREATE_USER_DUPLICATE_ERROR_RESPONSE, f'Ожидалcя ответ {UserData.CREATE_USER_DUPLICATE_ERROR_RESPONSE}, а вернулся {response.json()}'

    @pytest.mark.parametrize("param", [
        pytest.param("email"),
        pytest.param("password"),
        pytest.param("name")
    ])
    @allure.title("Создание пользователя без параметра {param} возвращает ошибку 403")
    @allure.description("Проверяем, что при попытке создания пользователя без обязательного параметра в теле запроса возвращается ошибка 403 и корректное сообщение об ошибке")
    def test_create_user_without_required_param_returns_error_403(self, param):
        body = UserFactory.default_body_with_random_params()
        response = UserApi.create_user(ChangeTestDataHelper.remove_param_from_body(body=body, key=param))

        assert response.status_code == 403, f'Ожидался статус код 403, а вернулся {response.status_code}'
        assert response.json() == UserData.CREATE_USER_MISSING_PARAMS_RESPONSE, f'Ожидалcя ответ {UserData.CREATE_USER_MISSING_PARAMS_RESPONSE}, а вернулся {response.json()}'
