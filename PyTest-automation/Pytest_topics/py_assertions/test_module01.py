
def test_a1():
    assert 4 <= 5
    assert 4 != 3


def test_a2():
    assert 1


def test_a3():
    assert "abcd" == 'abcd'


def test_a4():
    assert ((3-1)*4/2) == 4.0


def test_a5():
    assert 1 in divmod(9, 5)
    assert 'ppy' not in "this is a pytest"
    assert [1, 2] in [1, 2, 3]  # Fails, will to check in sub-list
    assert [1, 2] in [1, [1, 2], 2, 4]  # Pass

