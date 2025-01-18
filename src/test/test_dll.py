import pytest

from dsa.dll import LinkedList

from dsa.dll import Node, EmptyList, OutOfBounds, InconsistentState


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def populated_list():
    ll = LinkedList()
    ll.insert(0, "a")
    ll.insert(1, "b")
    ll.insert(2, "c")
    return ll


def test_insert_head(empty_list):
    node = empty_list.insert(0, "head")
    assert empty_list.length == 1
    assert empty_list.head == node
    assert empty_list.tail == node
    assert node.data == "head"


def test_insert_tail(populated_list):
    node = populated_list.insert(3, "tail")
    assert populated_list.length == 4
    assert populated_list.tail == node
    assert node.data == "tail"
    assert populated_list.traverse(3).data == "tail"


def test_insert_middle(populated_list):
    node = populated_list.insert(1, "middle")
    assert populated_list.length == 4
    assert populated_list.traverse(1) == node
    assert node.data == "middle"
    assert populated_list.traverse(0).next == node
    assert node.prev == populated_list.traverse(0)


def test_insert_out_of_bounds(empty_list):
    with pytest.raises(OutOfBounds):
        empty_list.insert(2, "fail")


def test_remove_head(populated_list):
    data = populated_list.remove(0)
    assert data == "a"
    assert populated_list.length == 2
    assert populated_list.head.data == "b"


def test_remove_tail(populated_list):
    data = populated_list.remove(2)
    assert data == "c"
    assert populated_list.length == 2
    assert populated_list.tail.data == "b"


def test_remove_middle(populated_list):
    data = populated_list.remove(1)
    assert data == "b"
    assert populated_list.length == 2
    assert populated_list.traverse(1).data == "c"


def test_remove_empty_list(empty_list):
    with pytest.raises(EmptyList):
        empty_list.remove(0)


def test_traverse_head(populated_list):
    node = populated_list.traverse(0)
    assert node.data == "a"


def test_traverse_tail(populated_list):
    node = populated_list.traverse(2)
    assert node.data == "c"


def test_traverse_middle(populated_list):
    node = populated_list.traverse(1)
    assert node.data == "b"


def test_traverse_out_of_bounds(populated_list):
    with pytest.raises(OutOfBounds):
        populated_list.traverse(5)


def test_remove_only_node(empty_list):
    empty_list.insert(0, "solo")
    data = empty_list.remove(0)
    assert data == "solo"
    assert empty_list.length == 0
    assert empty_list.head is None
    assert empty_list.tail is None


def test_inconsistent_state(empty_list):
    empty_list._head = None
    empty_list._tail = Node("corrupt")
    with pytest.raises(InconsistentState):
        empty_list.remove(0)
