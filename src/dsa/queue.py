"""
This module provides implementations for a queue.
"""

from __future__ import annotations
from typing import Any

from dsa.dll import LinkedList


class Queue:
    def __init__(self) -> None:
        """First-in-first-out (FIFO) linear data structure."""
        self._lst = LinkedList()

    def enqueue(self, value: Any) -> None:
        """Add an element to the back of the queue."""
        self._lst.insert(self._lst.length, value)

    def dequeue(self) -> Any:
        """Remove an element from the front of the queue."""
        if self._lst.length == 0:
            raise Exception("Cannot dequeue an empty queue")
        return self._lst.remove(0)

    def peek(self) -> Any:
        """Get the element at the front of the queue without removing it."""
        if self._lst.length == 0:
            raise Exception("Cannot peek an empty queue")
        return self._lst.traverse(0).data

    def contains(self, value: Any) -> bool:
        """Returns True if the queue contains the specified value"""
        return self._lst.contains(value)

    def is_empty(self) -> bool:
        """Returns True if the queue is empty"""
        return self._lst.length == 0
