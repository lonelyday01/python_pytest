import pytest
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.sanity
def test_str01():
    num = 9 / 4
    s1 = "I like pytest " + "automation"
    assert str(num) == "2.25"
    assert s1 == "I like pytest automation"
    assert s1 + str(num) == "I like pytest automation2.25"


@pytest.mark.sanity
def test_str02():
    letters = "abcdefghijklmnñopqrstuvwxyz"
    assert len(letters) == 27


def test_str03():
    letters = "abcdefghijklmnñopqrstuvwxyz"
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[26]


@pytest.mark.sanity
@pytest.mark.str
def test_strslice():
    letters = "abcdefghijklmnñopqrstuvwxyz"
    assert letters[:] == letters
    assert letters[10:] == "klmnñopqrstuvwxyz"
    assert letters[-3:] == "xyz"
    assert letters[:21:5] == "afkot"


def test_strsplit():
    s1 = "Python,Pytest and Automation"
    assert s1.split() == ['Python,Pytest', "and", "Automation"]
    assert s1.split(',') == ["Python", "Pytest and Automation"]


def test_strjoin():
    s1 = "Python,Pytest and Automation"
    l1 = ['Python,Pytest', "and", "Automation"]
    l2 = ["Python", "Pytest and Automation"]
    assert " ".join(l1) == s1
    assert ",".join(l2) == s1
