import pytest
import allure
from basicsteps import BasicSteps as bs
from assertionbear import AssertionBear as ab


@allure.title("Delete existing bear")
@pytest.mark.parametrize('bear_name', ['',  'testtest'])
def test_delete_existing_bear(bear_name):
    bear = bs.create_bear()
    assert ab.check_id_returns_after_creation(bear), f"Bear was not created"
    update_response = bs.update_bear_with_specified_parameter(int(bear.content), bear_name=bear_name)
    assert ab.check_that_operation_returns_ok(update_response), f"Bear was not updated"
    delete_response = bs.get_bear_by_id(int(bear.content))
    assert ab.check_user_updated_with_specified_name(delete_response, bear_name), \
        f"It's impossible to get update bear  with name {bear_name}"