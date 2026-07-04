from faker import Faker
from random import randint

class UserFactory:
    @staticmethod
    def default_body_with_random_params():
        faker = Faker()
        return {
            "email": faker.email(domain='stellarburgers.com'),
            "password": faker.password(),
            "name": faker.user_name() + str(randint(100, 999))
        }
    
class OrderFactory:
    @staticmethod
    def order_body_with_ingredients(ingredient_list):
        return {
            "ingredients": ingredient_list[:3]
        }
    
    @staticmethod
    def order_body_without_ingredients():
        return {
            "ingredients": []
        }
    
    @staticmethod
    def order_body_with_incorrect_ingredient():
        return {
            "ingredients": ["INCORRECT"]
        }    
    

class ChangeTestDataHelper:
    @staticmethod
    def remove_param_from_body(body: dict, key: str):
        body = body.copy()
        body.pop(key)
        return body
    
    @staticmethod
    def modify_param_from_body(body: dict, key: str, value: str):
        body = body.copy()
        body[key] = value
        return body