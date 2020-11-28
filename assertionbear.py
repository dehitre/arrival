class AssertionBear:
    @staticmethod
    def check_id_returns_after_creation(response):
        if response.status_code == 200 and int(response.content) > 0:
            return True
        return False

    @staticmethod
    def check_user_created_with_specified_type(response, bear_type):
        if response.status_code == 200 and response.content.decode('ascii') != 'null' and response.json()["bear_type"] \
                == bear_type:
            return True
        return False

    @staticmethod
    def check_user_created_with_specified_age(response, bear_age):
        if response.status_code == 200 and response.content.decode('ascii') != 'null' and response.json()["bear_age"] \
                == bear_age:
            return True
        return False

    @staticmethod
    def check_user_created_with_unsupported_age(response):
        if response.status_code == 200 and response.content.decode('ascii') != 'null' and response.json()["bear_age"] \
                == 0:
            return True
        return False

    @staticmethod
    def check_user_created_with_specified_name(response, bear_name):
        if response.status_code == 200 and response.content.decode('ascii') != 'null' and response.json()["bear_name"] \
                == bear_name.upper():
            return True
        return False

    @staticmethod
    def check_ok_returns_after_deletion(response):
        if response.status_code == 200 and response.content.decode('ascii') == 'OK':
            return True
        return False
