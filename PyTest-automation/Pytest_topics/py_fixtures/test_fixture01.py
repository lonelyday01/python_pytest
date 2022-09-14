import pytest


@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ['New York', 'London', 'Singapore', 'Guadalajara', 'Barcelona']
    return city


def test_getitem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Singapore', 'Barcelona']


def myreverse(lst):
    lst.reverse()
    return lst


def test_reverselist(setup_list):
    assert setup_list[::-2] == ['Barcelona', 'Singapore', 'New York']
    assert setup_list[::-1] == myreverse(setup_list)


@pytest.mark.xfail(reason="Known issue: usefixture cannot use the fixture's return value")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert setup_list[0]

