import pytest

from dsa.disjoint_set import DisjointSet


def test_initialization():
    elements = {1, 2, 3, 4, 5}
    ds = DisjointSet(elements)
    # Each element should be its own representative
    for element in elements:
        assert ds.find(element) == element


def test_union():
    elements = {1, 2, 3, 4, 5}
    ds = DisjointSet(elements)

    ds.union(1, 2)
    assert ds.find(1) == ds.find(2)

    ds.union(3, 4)
    assert ds.find(3) == ds.find(4)

    ds.union(2, 3)
    assert ds.find(1) == ds.find(4)


def test_multiple_unions():
    elements = {"a", "b", "c", "d", "e"}
    ds = DisjointSet(elements)

    ds.union("a", "b")
    ds.union("b", "c")

    assert ds.find("a") == ds.find("c")
    assert ds.find("d") != ds.find("a")

    ds.union("c", "d")
    assert ds.find("a") == ds.find("d")


def test_find_invalid_element():
    elements = {1, 2, 3}
    ds = DisjointSet(elements)

    with pytest.raises(ValueError):
        ds.find(4)


def test_union_invalid_element():
    elements = {1, 2, 3}
    ds = DisjointSet(elements)

    with pytest.raises(ValueError):
        ds.union(1, 5)


def test_redundant_union():
    elements = {1, 2, 3}
    ds = DisjointSet(elements)

    ds.union(1, 2)
    before_union = ds.find(1)
    ds.union(1, 2)
    assert ds.find(2) == before_union


def test_single_element_set():
    elements = {42}
    ds = DisjointSet(elements)

    assert ds.find(42) == 42


def test_disjoint_sets_remain_separate():
    elements = {1, 2, 3, 4}
    ds = DisjointSet(elements)

    ds.union(1, 2)
    ds.union(3, 4)

    assert ds.find(1) != ds.find(3)
    assert ds.find(2) != ds.find(4)
