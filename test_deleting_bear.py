import pytest
import allure
from basicsteps import BasicSteps as bs
from assertionbear import AssertionBear as ab


@allure.title("Delete existing bear")
def test_delete_existing_bear():
    bear = bs.create_bear()
    assert ab.check_id_returns_after_creation(bear)
    response = bs.delete_bear_by_id(int(bear.content))
    assert ab.check_ok_returns_after_deletion(response)


@allure.title("Delete non existing bear")
@pytest.mark.parametrize('bear_id', [5555, 0, -1, "qqq"])
def test_delete_non_existing_bear(bear_id):
    response = bs.delete_bear_by_id(bear_id)
    assert ab.check_ok_returns_after_deletion(response)
