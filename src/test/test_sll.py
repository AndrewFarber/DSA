import pytest

from dsa.sll import SinglyLinkedList


def test_sll_insert_empty():
    lst = SinglyLinkedList()
    assert lst.length == 0
    with pytest.raises(IndexError):
        lst.insert(1, "First")


def test_sll_insert_start():
    lst = SinglyLinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(0, "Second").data == "Second"
    assert lst.head.data == "Second"
    assert lst.tail.data == "First"
    assert lst.head.next == lst.tail
    assert lst.length == 2


def test_sll_insert_end():
    lst = SinglyLinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.head.data == "First"
    assert lst.head.next.data == "Second"
    assert lst.tail.data == "Third"
    assert lst.length == 3


def test_sll_insert_middle():
    lst = SinglyLinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(1, "Third").data == "Third"
    assert lst.head.data == "First"
    assert lst.head.next.data == "Third"
    assert lst.tail.data == "Second"
    assert lst.length == 3


def test_sll_search_empty():
    lst = SinglyLinkedList()
    with pytest.raises(IndexError):
        lst.search(0)


def test_sll_search_start():
    lst = SinglyLinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.search(0).data == "First"


def test_sll_search_end():
    lst = SinglyLinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.search(2).data == "Third"


def test_sll_search_middle():
    lst = SinglyLinkedList()
    assert lst.insert(0, "First").data == "First"
    assert lst.insert(1, "Second").data == "Second"
    assert lst.insert(2, "Third").data == "Third"
    assert lst.search(1).data == "Second"


def test_sll_remove_emtpy():
    lst = SinglyLinkedList()
    assert lst.length == 0
    with pytest.raises(IndexError):
        lst.remove(0)


def test_sll_remove_start():
    lst = SinglyLinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.remove(0).data == "First"
    assert lst.head.data == "Second"
    assert lst.tail.data == "Third"
    assert lst.length == 2


def test_sll_remove_end():
    lst = SinglyLinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.remove(2).data == "Third"
    assert lst.head.data == "First"
    assert lst.tail.data == "Second"
    assert lst.length == 2


def test_sll_remove_middle():
    lst = SinglyLinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.remove(1).data == "Second"
    assert lst.head.data == "First"
    assert lst.tail.data == "Third"
    assert lst.head.next == lst.tail
    assert lst.length == 2


def test_sll_find():
    lst = SinglyLinkedList()
    lst.insert(0, "First")
    lst.insert(1, "Second")
    lst.insert(2, "Third")
    assert lst.length == 3
    assert lst.find("First") == lst.head
    assert lst.find("Third") == lst.tail
    assert lst.find("Fourth") is None
