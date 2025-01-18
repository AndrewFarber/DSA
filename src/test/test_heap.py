import pytest

from dsa.heap import BinaryHeap, EmptyHeap


def test_min_heap_initialization():
    heap = BinaryHeap(type="min")
    assert heap.size == 0


def test_max_heap_initialization():
    heap = BinaryHeap(type="max")
    assert heap.size == 0


def test_min_heap_push():
    heap = BinaryHeap(type="min")
    heap.push(5)
    heap.push(3)
    heap.push(8)
    assert heap.size == 3
    assert heap._lst == [3, 5, 8]


def test_max_heap_push():
    heap = BinaryHeap(type="max")
    heap.push(5)
    heap.push(3)
    heap.push(8)
    # Internally stored as negative for max heap
    assert heap.size == 3
    assert heap._lst == [-8, -3, -5]


# Test Pop Operation
def test_min_heap_pop():
    heap = BinaryHeap(type="min")
    heap.push(5)
    heap.push(3)
    heap.push(8)
    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 8
    assert heap.size == 0


def test_max_heap_pop():
    heap = BinaryHeap(type="max")
    heap.push(5)
    heap.push(3)
    heap.push(8)
    assert heap.pop() == 8
    assert heap.pop() == 5
    assert heap.pop() == 3
    assert heap.size == 0


def test_pop_empty_heap():
    heap = BinaryHeap()
    with pytest.raises(EmptyHeap):
        heap.pop()


def test_push_pop_mixed_operations():
    heap = BinaryHeap(type="min")
    heap.push(4)
    heap.push(2)
    assert heap.pop() == 2
    heap.push(5)
    heap.push(1)
    assert heap.pop() == 1
    assert heap.pop() == 4
    assert heap.pop() == 5


def test_max_heap_push_pop_mixed_operations():
    heap = BinaryHeap(type="max")
    heap.push(4)
    heap.push(2)
    assert heap.pop() == 4
    heap.push(5)
    heap.push(1)
    assert heap.pop() == 5
    assert heap.pop() == 2
    assert heap.pop() == 1


def test_single_element_pop():
    heap = BinaryHeap()
    heap.push(10)
    assert heap.pop() == 10
    assert heap.size == 0


def test_duplicate_elements():
    heap = BinaryHeap()
    heap.push(5)
    heap.push(5)
    heap.push(5)
    assert heap.pop() == 5
    assert heap.pop() == 5
    assert heap.pop() == 5
    assert heap.size == 0
