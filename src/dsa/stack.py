"""
This module provides an implementation for a stack.
"""

from __future__ import annotations
from typing import Any

from dsa.sll import LinkedList


class Stack:
    def __init__(self) -> None:
        """
        Last-in-first-out (LIFO) linear collection of elements.
        """
        self._lst = LinkedList()

    def push(self, value: Any) -> None:
        """
        Add an element to the stack.
        """
        self._lst.insert(0, value)

    def pop(self) -> Any:
        """
        Remove an element from the stack.
        """
        if self._lst.length == 0:
            raise Exception("Cannot pop from an empty stack")
        return self._lst.remove(0)
