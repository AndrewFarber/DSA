import pytest

from dsa.fenwick_tree import FenwickTree


def test_fenwick_tree_initialization():
    array = [1, 2, 3, 4, 5]
    ft = FenwickTree(array)

    assert ft.prefix_sum(1) == 1
    assert ft.prefix_sum(2) == 3
    assert ft.prefix_sum(5) == 15


def test_fenwick_tree_range_query():
    array = [1, 2, 3, 4, 5]
    ft = FenwickTree(array)

    assert ft.range_query(1, 3) == 6
    assert ft.range_query(2, 4) == 9
    assert ft.range_query(1, 5) == 15
    assert ft.range_query(4, 4) == 4


def test_fenwick_tree_update():
    array = [1, 2, 3, 4, 5]
    ft = FenwickTree(array)

    # Update the 3rd element (1-based index) by adding 2
    ft.update(3, 2)

    assert ft.prefix_sum(3) == 8
    assert ft.prefix_sum(5) == 17

    # Test updated range queries
    assert ft.range_query(1, 3) == 8
    assert ft.range_query(3, 5) == 14


def test_edge_cases():
    # Test with an empty array
    ft = FenwickTree([])

    # Prefix sum should always be 0
    assert ft.prefix_sum(0) == 0

    # Test invalid indices for update
    with pytest.raises(IndexError):
        ft.update(1, 5)  # Update on an empty array

    # Test invalid indices for range_query
    with pytest.raises(IndexError):
        ft.range_query(0, 1)

    with pytest.raises(IndexError):
        ft.range_query(1, 6)


def test_single_element_array():
    """
    Test a Fenwick Tree with a single-element array.
    """
    array = [42]
    ft = FenwickTree(array)

    # Test prefix sum
    assert ft.prefix_sum(1) == 42

    # Test range query
    assert ft.range_query(1, 1) == 42

    # Test update
    ft.update(1, 8)  # Add 8 to the single element
    assert ft.prefix_sum(1) == 50
    assert ft.range_query(1, 1) == 50
