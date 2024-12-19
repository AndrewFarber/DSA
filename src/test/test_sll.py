import pytest

from dsa.sll import LinkedList


def test_sll_insert_empty():
    lst = LinkedList()
    assert lst.length == 0
    with pytest.raises(Exception):
        lst.insert(1, "First")


def test_sll_insert_start():
    lst = LinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(0, "Second").data == "Second"
    assert lst.head.data == "Second"
    assert lst.tail.data == "First"
    assert lst.head.next == lst.tail
    assert lst.length == 2


def test_sll_insert_end():
    lst = LinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.head.data == "First"
    assert lst.head.next.data == "Second"
    assert lst.tail.data == "Third"
    assert lst.length == 3


def test_sll_insert_middle():
    lst = LinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(1, "Third").data == "Third"
    assert lst.head.data == "First"
    assert lst.head.next.data == "Third"
    assert lst.tail.data == "Second"
    assert lst.length == 3


def test_sll_traverse_empty():
    lst = LinkedList()
    with pytest.raises(Exception):
        lst.traverse(0)


def test_sll_traverse_start():
    lst = LinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.traverse(0).data == "First"


def test_sll_traverse_end():
    lst = LinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.traverse(2).data == "Third"


def test_sll_traverse_middle():
    lst = LinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.traverse(1).data == "Second"


def test_sll_remove_emtpy():
    lst = LinkedList()
    assert lst.length == 0
    with pytest.raises(Exception):
        lst.remove(0)


def test_sll_remove_start():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.remove(0) == "First"
    assert lst.head.data == "Second"
    assert lst.tail.data == "Third"
    assert lst.length == 2


def test_sll_remove_end():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.remove(2) == "Third"
    assert lst.head.data == "First"
    assert lst.tail.data == "Second"
    assert lst.length == 2


def test_sll_remove_middle():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.remove(1) == "Second"
    assert lst.head.data == "First"
    assert lst.tail.data == "Third"
    assert lst.head.next == lst.tail
    assert lst.length == 2


def test_sll_find():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.find("First") == lst.head
    assert lst.find("Third") == lst.tail
    assert lst.find("Fourth") is None


def test_sll_contains():
    lst = LinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    lst.insert(3, None)
    assert lst.length == 4
    assert lst.contains("First") is True
    assert lst.contains("Third") is True
    assert lst.contains(None) is True
    assert lst.contains("Fourth") is False
