import pytest

from dsa.sll import LinkedList

from dsa.sll import EmptyList, OutOfBounds, InconsistentState


def test_insert_into_empty_list():
    ll = LinkedList()
    node = ll.insert(0, 10)
    assert node.data == 10
    assert ll.length == 1
    assert ll.head == node
    assert ll.tail == node


def test_insert_at_head():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(0, 20)
    assert ll.head.data == 20
    assert ll.head.next.data == 10
    assert ll.length == 2


def test_insert_at_tail():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 20)
    ll.insert(2, 30)
    assert ll.tail.data == 30
    assert ll.length == 3


def test_insert_in_middle():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 30)
    ll.insert(1, 20)
    assert ll.traverse(0).data == 10
    assert ll.traverse(1).data == 20
    assert ll.traverse(2).data == 30
    assert ll.length == 3


def test_insert_out_of_bounds():
    ll = LinkedList()
    with pytest.raises(OutOfBounds):
        ll.insert(1, 10)


def test_remove_only_node():
    ll = LinkedList()
    ll.insert(0, 10)
    data = ll.remove(0)
    assert data == 10
    assert ll.length == 0
    assert ll.head is None
    assert ll.tail is None


def test_remove_head():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 20)
    data = ll.remove(0)
    assert data == 10
    assert ll.head.data == 20
    assert ll.length == 1


def test_remove_tail():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 20)
    data = ll.remove(1)
    assert data == 20
    assert ll.tail.data == 10
    assert ll.length == 1


def test_remove_middle():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 20)
    ll.insert(2, 30)
    data = ll.remove(1)
    assert data == 20
    assert ll.traverse(0).data == 10
    assert ll.traverse(1).data == 30
    assert ll.length == 2


def test_remove_from_empty_list():
    ll = LinkedList()
    with pytest.raises(EmptyList):
        ll.remove(0)


def test_remove_out_of_bounds():
    ll = LinkedList()
    ll.insert(0, 10)
    with pytest.raises(OutOfBounds):
        ll.remove(2)


def test_traverse_valid_positions():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 20)
    ll.insert(2, 30)
    assert ll.traverse(0).data == 10
    assert ll.traverse(1).data == 20
    assert ll.traverse(2).data == 30


def test_traverse_empty_list():
    ll = LinkedList()
    with pytest.raises(EmptyList):
        ll.traverse(0)


def test_traverse_out_of_bounds():
    ll = LinkedList()
    ll.insert(0, 10)
    with pytest.raises(OutOfBounds):
        ll.traverse(2)


def test_insert_with_inconsistent_state():
    ll = LinkedList()
    ll._tail = None  # Manually breaking the state
    ll._length = 1
    with pytest.raises(AssertionError):
        ll.insert(1, 10)


def test_remove_with_inconsistent_state():
    ll = LinkedList()
    ll.insert(0, 10)
    ll._head = None  # Manually breaking the state
    with pytest.raises(InconsistentState):
        ll.remove(0)
