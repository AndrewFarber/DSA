"""
This module provides implementations for a singly linked lists.
"""

from __future__ import annotations
from typing import Any


class SLNode:
    def __init__(self, data: Any, next: SLNode | None = None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.length = 0
        self.head: SLNode | None = None
        self.tail: SLNode | None = None

    def search(self, index: int) -> SLNode:
        """Get the node at the specified index."""
        if self.length == 0:
            raise IndexError("List is empty")
        if not (0 <= index < self.length):
            raise IndexError("Index out of bounds")
        if self.head is None or self.tail is None:
            raise Exception("Linked list is in inconsistent state")

        if index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        else:
            node = self.head
            for _ in range(index):
                assert node is not None  # Inconsistent state
                node = node.next
            assert node is not None  # Inconsistent state
            return node

    def find(self, value: Any) -> SLNode | None:
        """
        Return the first node containing the data that matches
        the specified value.
        """
        if self.length == 0:
            raise IndexError("List is empty")
        if self.head is None or self.tail is None:
            raise Exception("Linked list is in inconsistent state")

        node = self.head
        while True:
            if node.data == value:
                return node
            elif node.next is None:
                return None
            else:
                node = node.next

    def insert(self, index: int, data: Any) -> SLNode:
        """
        Insert a node with the provided data at the specified index.
        Returns the new node.

        If the provided index matches the length of the array, a new node
        will be appended to the end.
        """
        # Insert first node
        if index == 0 and self.length == 0:
            n = SLNode(data)
            self.head = n
            self.tail = n
            self.length += 1
            return n

        # Insert at head
        if index == 0:
            h = self.head
            self.head = SLNode(data, next=h)
            self.length += 1
            return self.head

        # Insert at tail (i.e., Append)
        if index == self.length:
            n = SLNode(data)
            assert self.tail is not None  # Inconsistent state
            self.tail.next = n
            self.tail = n
            self.length += 1
            return self.tail

        # Insert in middle
        if 0 < index < self.length:
            before = self.search(index - 1)
            after = before.next
            new = SLNode(data, next=after)
            before.next = new
            self.length += 1
            return new

        raise IndexError("Index out of bounds")

    def remove(self, index: int) -> SLNode:
        """
        Remove the node at the specified index.
        Returns the removed node.
        """
        if self.length == 0:
            raise IndexError("List is empty")
        if self.head is None or self.tail is None:
            raise Exception("Linked list is in inconsistent state")

        # Remove only node
        if index == 0 and self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed

        # Remove at head
        if index == 0:
            removed = self.head
            self.head = self.head.next
            self.length -= 1
            return removed

        # Remove at tail
        if index == (self.length - 1):
            removed = self.tail
            before = self.search(self.length - 2)
            assert before is not None  # Inconsistent state
            before.next = None
            self.tail = before
            self.length -= 1
            return removed

        # Remove in middle
        if 0 < index < self.length - 1:
            before = self.search(index - 1)
            assert before is not None and before.next is not None  # Inconsistent state
            removed = before.next
            before.next = before.next.next
            self.length -= 1
            return removed

        raise IndexError("Index out of bounds")
