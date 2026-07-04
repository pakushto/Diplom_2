class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    CREATE_USER_URL = BASE_URL + "/api/auth/register"
    DELETE_USER_URL = BASE_URL + "/api/auth/user"
    LOGIN_USER_URL = BASE_URL + "/api/auth/login"
    PATCH_USER_URL = BASE_URL + "/api/auth/user"

    CREATE_ORDER_URL = BASE_URL + "/api/orders"
    GET_USER_ORDERS = BASE_URL + "/api/orders"

    GET_INGREDIENTS_URL = BASE_URL + "/api/ingredients"

