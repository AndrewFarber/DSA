import pytest

from dsa.dll import LinkedList


def test_dll_insert_empty():
    lst = LinkedList()
    assert lst.length == 0
    with pytest.raises(Exception):
        lst.insert(1, "First")


def test_dll_insert_start():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(0, "Second")
    assert lst.head.data == "Second"
    assert lst.tail.data == "First"
    assert lst.head.next == lst.tail
    assert lst.tail.prev == lst.head
    assert lst.length == 2


def test_dll_insert_end():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.head.data == "First"
    assert lst.head.next.data == "Second"
    assert lst.head.next.next.data == "Third"
    assert lst.tail.data == "Third"
    assert lst.tail.prev.data == "Second"
    assert lst.tail.prev.prev.data == "First"
    assert lst.length == 3


def test_dll_insert_middle():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Third")
    lst.insert(1, "Second")
    assert lst.head.data == "First"
    assert lst.head.next.data == "Second"
    assert lst.head.next.next.data == "Third"
    assert lst.tail.data == "Third"
    assert lst.tail.prev.data == "Second"
    assert lst.tail.prev.prev.data == "First"
    assert lst.length == 3


def test_dll_traverse_empty():
    lst = LinkedList()
    with pytest.raises(Exception):
        lst.traverse(0)


def test_dll_traverse_start():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.traverse(0).data == "First"
    assert lst.traverse(0).next.data == "Second"
    assert lst.traverse(0).next.next.data == "Third"


def test_dll_traverse_end():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.traverse(2).data == "Third"
    assert lst.traverse(2).prev.data == "Second"
    assert lst.traverse(2).prev.prev.data == "First"


def test_dll_traverse_middle():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.traverse(1).data == "Second"
    assert lst.traverse(1).prev.data == "First"
    assert lst.traverse(1).next.data == "Third"


def test_dll_remove_emtpy():
    lst = LinkedList()
    assert lst.length == 0
    with pytest.raises(Exception):
        lst.remove(0)


def test_dll_remove_start():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    assert lst.length == 2
    lst.remove(0)
    assert lst.head.data == "Second"
    assert lst.tail.data == "Second"
    assert lst.head.next is None
    assert lst.head.prev is None
    assert lst.tail.next is None
    assert lst.tail.prev is None
    assert lst.length == 1


def test_dll_remove_end():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    assert lst.length == 2
    lst.remove(1)
    assert lst.head.data == "First"
    assert lst.tail.data == "First"
    assert lst.head.next is None
    assert lst.head.prev is None
    assert lst.tail.next is None
    assert lst.tail.prev is None
    assert lst.length == 1


def test_dll_remove_middle():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Third")
    lst.insert(1, "Second")
    lst.remove(1)
    assert lst.head.data == "First"
    assert lst.head.next.data == "Third"
    assert lst.tail.data == "Third"
    assert lst.tail.prev.data == "First"
    assert lst.length == 2

