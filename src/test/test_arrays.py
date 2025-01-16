import pytest

from dsa.arrays import StaticArray, DynamicArray


def test_static_array_initialization():
    array = StaticArray(5)
    assert array.size() == 5
    assert array.array == [None, None, None, None, None]


def test_static_array_invalid_initialization():
    with pytest.raises(ValueError):
        StaticArray(0)
    with pytest.raises(ValueError):
        StaticArray(-5)


def test_static_array_get_set_valid():
    array = StaticArray(3)
    array.set(0, "a")
    array.set(1, "b")
    array.set(2, "c")
    assert array.get(0) == "a"
    assert array.get(1) == "b"
    assert array.get(2) == "c"


def test_static_array_get_set_invalid():
    array = StaticArray(3)
    with pytest.raises(IndexError):
        array.get(-1)
    with pytest.raises(IndexError):
        array.get(3)
    with pytest.raises(IndexError):
        array.set(3, "x")


def test_static_array_clear():
    array = StaticArray(3)
    array.set(0, 1)
    array.set(1, 2)
    array.set(2, 3)
    array.clear()
    assert array.array == [None, None, None]


def test_static_array_contains():
    array = StaticArray(3)
    array.set(0, "x")
    array.set(1, "y")
    array.set(2, "z")
    assert array.contains("x") is True
    assert array.contains("a") is False


def test_dynamic_array_initialization():
    array = DynamicArray(2)
    assert array.size() == 2


def test_dynamic_array_append():
    array = DynamicArray(2)
    array.set(0, "a")
    array.set(1, "b")
    array.append("c")
    assert array.size() == 3
    assert array.get(0) == "a"
    assert array.get(1) == "b"
    assert array.get(2) == "c"


def test_dynamic_array_insert():
    array = DynamicArray(2)
    array.set(0, "b")
    array.set(1, "c")
    array.insert("a")
    assert array.size() == 3
    assert array.get(0) == "a"
    assert array.get(1) == "b"
    assert array.get(2) == "c"


def test_dynamic_array_delete():
    array = DynamicArray(3)
    array.set(0, "x")
    array.set(1, "y")
    array.set(2, "z")
    array.delete(1)
    assert array.size() == 2
    assert array.get(0) == "x"
    assert array.get(1) == "z"


def test_dynamic_array_delete_invalid():
    array = DynamicArray(2)
    with pytest.raises(IndexError):
        array.delete(5)
    with pytest.raises(IndexError):
        array.delete(-1)


def test_dynamic_array_contains():
    array = DynamicArray(3)
    array.set(0, 10)
    array.set(1, 20)
    array.set(2, 30)
    assert array.contains(20) is True
    assert array.contains(40) is False


def test_dynamic_array_clear():
    array = DynamicArray(3)
    array.set(0, 1)
    array.set(1, 2)
    array.set(2, 3)
    array.clear()
    for i in range(array.size()):
        assert array.get(i) is None
