from dsa.heap import BinaryHeap


def test_min_heap():
    h = BinaryHeap(type="min")
    h.push(5)
    h.push(4)
    h.push(3)
    h.push(2)
    h.push(1)
    h.push(0)
    h.push(-1)
    assert h.pop() == -1
    assert h.pop() == 0
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 3
    assert h.pop() == 4
    assert h.pop() == 5


def test_max_heap():
    h = BinaryHeap(type="max")
    h.push(-1)
    h.push(0)
    h.push(1)
    h.push(2)
    h.push(3)
    h.push(4)
    h.push(5)
    assert h.pop() == 5
    assert h.pop() == 4
    assert h.pop() == 3
    assert h.pop() == 2
    assert h.pop() == 1
    assert h.pop() == 0
    assert h.pop() == -1
