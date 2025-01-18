import pytest

from dsa.disjoint_set import DisjointSet


@pytest.fixture
def disjoint_set():
    return DisjointSet(["a", "b", "c", "d", "e"])


def test_initialization(disjoint_set):
    assert disjoint_set.find("a") == "a"
    assert disjoint_set.find("b") == "b"
    assert disjoint_set.find("c") == "c"
    assert disjoint_set.find("d") == "d"
    assert disjoint_set.find("e") == "e"


def test_union(disjoint_set):
    disjoint_set.union("a", "b")
    assert disjoint_set.find("a") == disjoint_set.find("b")

    disjoint_set.union("c", "d")
    assert disjoint_set.find("c") == disjoint_set.find("d")

    disjoint_set.union("b", "c")
    assert disjoint_set.find("a") == disjoint_set.find("d")


def test_redundant_union(disjoint_set):
    disjoint_set.union("a", "b")
    disjoint_set.union("a", "b")  # Redundant
    assert disjoint_set.find("a") == disjoint_set.find("b")


def test_find_nonexistent_element(disjoint_set):
    with pytest.raises(ValueError):
        disjoint_set.find("z")


def test_union_nonexistent_element(disjoint_set):
    with pytest.raises(ValueError):
        disjoint_set.union("a", "z")


def test_duplicate_elements():
    ds = DisjointSet(["a", "a", "b", "b", "c"])
    assert ds.find("a") == "a"
    assert ds.find("b") == "b"
    assert ds.find("c") == "c"


def test_single_element_set():
    ds = DisjointSet(["x"])
    assert ds.find("x") == "x"
    with pytest.raises(ValueError):
        ds.find("y")


def test_empty_set():
    ds = DisjointSet([])
    with pytest.raises(ValueError):
        ds.find("x")


def test_path_compression(disjoint_set):
    disjoint_set.union("a", "b")
    disjoint_set.union("b", "c")
    disjoint_set.union("c", "d")
    # Path compression should flatten the structure
    assert disjoint_set.find("a") == disjoint_set.find("d")


def test_large_union():
    elements = list(range(1000))
    ds = DisjointSet(elements)

    for i in range(0, 999):
        ds.union(i, i + 1)

    assert ds.find(0) == ds.find(999)
