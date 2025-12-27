class UserData:
    CREATE_USER_BODY = {
        "email": "maks_data_34451@yandex.ru",
        "password": "password",
        "name": "Username"
    }

    CREATE_USER_DUPLICATE_ERROR_RESPONSE = {
        "success": False,
        "message": "User already exists"
    }

    CREATE_USER_MISSING_PARAMS_RESPONSE = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    LOGIN_USER_BODY = {
        "email": "maks_data_34451@yandex.ru",
        "password": "password"
    }

    LOGIN_USER_INCORRECT_PARAMS_RESPONSE = {
        "success": False,
        "message": "email or password are incorrect"
    }

    PATCH_USER_BODY = {
        "email": "test123@greathouse.ru",
        "name": "Username"
    }

    PATCH_USER_UNAUTHORIZED_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }

class OrderData:
    CREATE_ORDER_BODY = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa73",
            "61c0c5a71d1f82001bdaaa6c"
        ]
    }

    CREATE_ORDER_WITHOUT_INGREDIENTS_RESPONSE = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    GET_USER_ORDERS_WITHOUT_AUTH_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }