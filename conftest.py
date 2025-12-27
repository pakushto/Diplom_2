import pytest
from api.user_api import UserApi
from api.ingredient_api import IngredientApi
from api.order_api import OrderApi
from helper import UserFactory, OrderFactory


@pytest.fixture(scope='function')
def cleanup_user():
    access_tokens = []
    yield access_tokens
    for access_token in access_tokens:
        response = UserApi.delete_user(access_token=access_token)
        assert response.status_code == 202

@pytest.fixture(scope='function')
def create_user(cleanup_user):
    body = UserFactory.default_body_with_random_params()
    response = UserApi.create_user(body=body)
    access_token = response.json()["accessToken"]

    yield {
        "body": body,
        "access_token": access_token,
        "login_body": {
            "email": body["email"],
            "password": body["password"],
        }
    }

    cleanup_user.append(access_token)

@pytest.fixture(scope='function')
def ingredient_list():
    response = IngredientApi.get_ingedients()
    ingredient_list = [item["_id"] for item in response.json()["data"]]
    return ingredient_list


@pytest.fixture(scope='function')
def create_user_order(create_user, ingredient_list):
    body = OrderFactory.order_body_with_ingredients(ingredient_list)
    response = OrderApi.create_order(body, create_user["access_token"])
    return {
        "access_token": create_user["access_token"]
    }