"""
This module provides implementations for a stack using a linked lists.
"""

from __future__ import annotations
from typing import Any

from dsa.sll import SinglyLinkedList


class Stack:
    def __init__(self) -> None:
        """Last-in-first-out (LIFO) linear data structure."""
        self._lst = SinglyLinkedList()

    def push(self, value: Any) -> None:
        """Add an element to the stack"""
        self._lst.insert(0, value)

    def pop(self) -> Any:
        """Remove an element from the stack"""
        if self._lst.length == 0:
            raise Exception("Cannot pop from an empty stack")
        return self._lst.remove(0).data

    def peek(self) -> Any:
        """View the first element in the stack without removing it"""
        if self._lst.length == 0:
            raise Exception("Cannot peek from an empty stack")
        return self._lst.search(0).data

    def search(self, value: Any) -> Any:
        """
        Search the stack for the specified value and return it.
        Returns None if the value is not in the stack.
        """
        val = self._lst.find(value)
        if val is None:
            return None
        return val.data

    def size(self) -> int:
        """Return the number of elements in the stack. An empty stack returns zero."""
        return self._lst.length
