import pytest
import allure
from basicsteps import BasicSteps as bs
from assertionbear import AssertionBear as ab


@allure.title("Create bear with different types")
@pytest.mark.parametrize('bear_type', ["BLACK", "BROWN", "POLAR", "GUMMY"])
def test_creating_bear_with_different_types(bear_type):
    bear = bs.create_bear_with_specified_type(bear_type)
    assert ab.check_id_returns_after_creation(bear)
    response = bs.get_bear_by_id(int(bear.content))
    assert ab.check_user_created_with_specified_type(response, bear_type)


@allure.title("Create bear with age is between 0 and 100")
@pytest.mark.parametrize('bear_age', [0, 1, 100])
def test_creating_bear_with_age_is_between_0_and_100(bear_age):
    bear = bs.create_bear_with_specified_age(bear_age)
    assert ab.check_id_returns_after_creation(bear)
    response = bs.get_bear_by_id(int(bear.content))
    assert ab.check_user_created_with_specified_age(response, bear_age)


@allure.title("Create bear with 0 age in case of invalid value")
@pytest.mark.parametrize('bear_age', [-1, 101])
def test_creating_bear_with_0_age_in_case_of_invalid_value(bear_age):
    bear = bs.create_bear_with_specified_age(bear_age)
    assert ab.check_id_returns_after_creation(bear)
    response = bs.get_bear_by_id(int(bear.content))
    assert ab.check_user_created_with_unsupported_age(response)


@allure.title("Create bear with name with spaces")
@pytest.mark.parametrize('bear_name', ['', ' ', ' test ', 'test test'])
def test_creating_bear_with_name_with_spaces(bear_name):
    bear = bs.create_bear_with_name_with_spaces(bear_name)
    assert ab.check_id_returns_after_creation(bear)
    response = bs.get_bear_by_id(int(bear.content))
    assert ab.check_user_created_with_specified_name(response, bear_name)
