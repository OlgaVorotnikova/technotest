import pytest


def test_set1_intersection():
    set11 = {1, 2, 3, 4, 5}
    set12 = {5, 6}
    assert set11.intersection(set12) == {5}


def test_set2_difference():
    set21 = {'v', 'k', 'o', 'n', 't'}
    set22 = {'v', 'k'}
    assert set21.difference(set22) == {'o', 'n', 't'}


def test_set3_remove_negative():
    set3 = {'a', 'b', 'c'}
    try:
        assert set3.remove('d')
    except KeyError:
        pass


def test_float1_add():
    n1 = 1.0
    n2 = 2
    assert (n1 + n2) == 3.0


def test_float2_multiplication():
    n1 = 3.0
    n2 = 3.1
    assert (n1 * n2) == 9.3


@pytest.mark.parametrize('num', [-500.0, -1.0, 0.0, 1.0, 1000.0])
def test_float3_is_integer(num):
    assert num.is_integer()

