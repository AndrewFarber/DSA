import pytest

from dsa.stacks import Stack


def test_stack_push():
    s = Stack()
    assert s.push("First") is None
    assert s.push("Second") is None
    assert s.push("Third") is None


def test_stack_pop():
    s = Stack()
    with pytest.raises(Exception):
        s.pop()
    assert s.push("First") is None
    assert s.push("Second") is None
    assert s.push("Third") is None
    assert s.pop() == "Third"
    assert s.pop() == "Second"
    assert s.pop() == "First"
    with pytest.raises(Exception):
        s.pop()


def test_stack_peek():
    pass
    s = Stack()
    with pytest.raises(Exception):
        s.peek()
    assert s.push("First") is None
    assert s.push("Second") is None
    assert s.push("Third") is None
    assert s.peek() == "Third"


def test_stack_search():
    s = Stack()
    assert s.push("First") is None
    assert s.push("Second") is None
    assert s.push("Third") is None
    assert s.search("First") == "First"
    assert s.search("Second") == "Second"
    assert s.search("Third") == "Third"
    assert s.pop() == "Third"
    assert s.pop() == "Second"
    assert s.pop() == "First"


def test_stack_size():
    s = Stack()
    assert s.push("First") is None
    assert s.push("Second") is None
    assert s.push("Third") is None
    assert s.size() == 3
