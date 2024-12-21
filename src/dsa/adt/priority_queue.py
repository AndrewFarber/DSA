"""
This module provides an implementation for a priority queue.
"""

from typing import Any

from dsa.heap import BinaryHeap


class PriorityQueue:
    def __init__(self) -> None:
        """
        Linear collection of elements with priority.
        """
        self._heap = BinaryHeap()

    def enqueue(self, value: Any) -> None:
        """
        Add a value to the priority queue.
        """
        self._heap.push(value)

    def dequeue(self) -> Any:
        """
        Remove a value from the priority queue.
        """
        if self._heap.size == 0:
            raise Exception("Cannot dequeue from an empty priority queue")
        return self._heap.pop()
