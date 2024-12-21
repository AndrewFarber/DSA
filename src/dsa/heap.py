"""
This module provides implementation for a binary heap.
"""

from __future__ import annotations
from typing import Any, Literal


class EmptyHeap(Exception):
    pass


class OutOfBounds(Exception):
    pass


class BinaryHeap:
    def __init__(self, type: Literal["min", "max"] = "min") -> None:
        """
        Instantiate an empty binary heap.
        """
        self._type = type
        self._lst: list = list()

    @property
    def size(self) -> int:
        """
        The number of nodes in the heap
        """
        return len(self._lst)

    def push(self, value: Any) -> None:
        if self._type == "max":
            value = -1 * value

        self._lst.append(value)  # Add value to end of list
        self._up(self.size - 1)  # Move up through list

    def pop(self) -> Any:
        if self.size == 0:
            raise EmptyHeap
        elif self.size == 1:
            value = self._lst.pop()
        else:
            self._swap(0, self.size - 1)  # Swap first/last value in list
            value = self._lst.pop()  # Remove last value in list
            self._down(0)  # Move down through list

        if self._type == "max":
            value = -1 * value
        return value

    def _swap(self, index_1: int, index_2: int) -> None:
        value_1 = self._lst[index_1]
        value_2 = self._lst[index_2]
        self._lst[index_1] = value_2
        self._lst[index_2] = value_1

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def _up(self, index: int) -> None:
        if not (0 <= index < self.size):
            return

        parent_index = self._parent(index)
        while parent_index >= 0:
            index_value = self._lst[index]
            parent_value = self._lst[parent_index]

            if index_value < parent_value:
                self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent(index)

    def _down(self, index: int) -> None:
        if not (0 <= index < self.size):
            return

        left_child_index = self._left_child(index)
        while left_child_index < self.size:
            index_value = self._lst[index]
            left_child_value = self._lst[left_child_index]
            right_child_index = self._right_child(index)

            if right_child_index < self.size:
                right_child_value = self._lst[right_child_index]
            else:
                right_child_value = None

            # Swap right
            if right_child_value is not None and right_child_value < left_child_value:
                if right_child_value < index_value:
                    self._swap(index, right_child_index)
                index = right_child_index
                left_child_index = self._left_child(index)
            # Swap left
            else:
                if left_child_value < index_value:
                    self._swap(index, left_child_index)
                index = left_child_index
                left_child_index = self._left_child(index)
