import allure


def check_that_response_is_ok(response):
    if response.status_code == 200 and response.content.decode('ascii') != 'null':
        return True
    return False


class AssertionBear:
    @staticmethod
    @allure.step("Check that creation was successful")
    def check_id_returns_after_creation(response):
        if response.status_code == 200 and int(response.content) > 0:
            return True
        return False

    @staticmethod
    @allure.step("Check that bear created with specified type")
    def check_user_created_with_specified_type(response, bear_type):
        if check_that_response_is_ok(response) and response.json()["bear_type"] \
                == bear_type:
            return True
        return False

    @staticmethod
    @allure.step("Check that bear created with specified age")
    def check_user_created_with_specified_age(response, bear_age):
        if check_that_response_is_ok(response) and response.json()["bear_age"] \
                == bear_age:
            return True
        return False

    @staticmethod
    @allure.step("Check that bear created with unsupported age")
    def check_user_created_with_unsupported_age(response):
        if check_that_response_is_ok(response) and response.json()["bear_age"] \
                == 0:
            return True
        return False

    @staticmethod
    @allure.step("Check that bear created with specified name and name is upper case")
    def check_user_created_with_specified_name(response, bear_name):
        if check_that_response_is_ok(response) and response.json()["bear_name"] \
                == bear_name.upper():
            return True
        return False

    @staticmethod
    @allure.step("Check that bear updated with specified name and name is case sensitive")
    def check_user_updated_with_specified_name(response, bear_name):
        if check_that_response_is_ok(response) and response.json()["bear_name"] \
                == bear_name:
            return True
        return False

    @staticmethod
    @allure.step("Check that bear was deleted")
    def check_that_operation_returns_ok(response):
        if check_that_response_is_ok(response) and response.content.decode('ascii') == 'OK':
            return True
        return False
