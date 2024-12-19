import pytest

from dsa.queue import Queue


def test_queue_enqueue():
    q = Queue()
    assert q.enqueue("First") is None
    assert q.enqueue("Second") is None
    assert q.enqueue("Third") is None


def test_queue_dequeue():
    q = Queue()
    with pytest.raises(Exception):
        q.dequeue()
    assert q.enqueue("First") is None
    assert q.enqueue("Second") is None
    assert q.enqueue("Third") is None
    assert q.dequeue() == "First"
    assert q.dequeue() == "Second"
    assert q.dequeue() == "Third"
    with pytest.raises(Exception):
        q.dequeue()


def test_queue_peek():
    pass
    q = Queue()
    with pytest.raises(Exception):
        q.peek()
    assert q.enqueue("First") is None
    assert q.enqueue("Second") is None
    assert q.enqueue("Third") is None
    assert q.peek() == "First"


def test_queue_contains():
    q = Queue()
    assert q.enqueue("First") is None
    assert q.enqueue("Second") is None
    assert q.enqueue("Third") is None
    assert q.contains("Second") is True
