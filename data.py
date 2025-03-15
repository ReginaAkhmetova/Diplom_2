class ValidUser:
    email = ("polosatik@ya.ru",)
    password = ("qwerty1",)
    name = "polosatik"


class DataMessage:
    # пользователь уже существует
    MES_USER_EXIST = {"success": False, "message": "User already exists"}
    # нет одного из полей
    MES_NO_ONE_OF_THE_FIELDS = {
        "success": False,
        "message": "Email, password and name are required fields",
    }
    # неверные логин или пароль
    MES_EMAIL_OR_PASSWORD_ARE_INCORRECT = {
        "success": False,
        "message": "email or password are incorrect",
    }
    # изменение данных без авторизации
    MES_YOU_SHOULD_BE_AUTHORISED = {
        "success": False,
        "message": "You should be authorised",
    }
    MES_ONE_OR_MORE_IDS_PROVIDED_INCORRECT = {
        "success": False,
        "message": "One or more ids provided are incorrect",
    }

class DataIngredients:
    PAILOAD = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa71",
            "61c0c5a71d1f82001bdaaa73",
        ]
    }
    INVALID_PAYLOAD = {
            "ingredients": ["61c0c5a71d1f82001bdaaa00"],
    }
