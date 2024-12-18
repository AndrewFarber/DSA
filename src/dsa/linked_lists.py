"""
This module provides implementations for singly and doubly linked lists.
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


class DLNode:
    def __init__(
        self, data: Any, prev: DLNode | None = None, next: DLNode | None = None
    ):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head: DLNode | None = None
        self.tail: DLNode | None = None

    def search(self, index: int) -> DLNode:
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

    def insert(self, index: int, data: Any) -> None:
        """
        Insert a node with the provided data at the specified index.
        If the provided index matches the length of the array, a new node
        will be appended to the end.
        """
        # Insert first node
        if index == 0 and self.length == 0:
            n = DLNode(data)
            self.head = n
            self.tail = n
            self.length += 1
            return

        # Insert at head
        if index == 0:
            h = self.head
            assert h is not None  # Inconsistent state
            self.head = DLNode(data, next=h)
            h.prev = self.head
            self.length += 1
            return

        # Insert at tail (i.e., Append)
        if index == self.length:
            assert self.tail is not None  # Inconsistent state
            n = DLNode(data, prev=self.tail, next=None)
            self.tail.next = n
            self.tail = n
            self.length += 1
            return

        # Insert in middle
        if 0 < index < self.length:
            before = self.search(index - 1)
            after = before.next
            assert before is not None and after is not None  # Inconsistent state
            new = DLNode(data, prev=before, next=after)
            before.next = new
            after.prev = new
            self.length += 1
            return

        raise IndexError("Index out of range")

    def remove(self, index: int) -> None:
        """Remove the node at the specified index."""
        if self.length == 0:
            raise IndexError("List is empty")

        # Remove only node
        if index == 0 and self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        # Remove at head
        if index == 0:
            assert self.head is not None  # Inconsistent state
            assert self.head.next is not None  # Inconsistent state
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return

        # Remove at tail
        if index == (self.length - 1):
            assert self.tail is not None  # Inconsistent state
            assert self.tail.prev is not None  # Inconsistent state
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return

        # Remove in middle
        if 0 < index < self.length - 1:
            before = self.search(index - 1)
            assert before is not None  # Inconsistent state
            current = before.next
            assert current is not None  # Inconsistent state
            after = current.next
            assert after is not None  # Inconsistent state
            before.next = after
            after.prev = before
            self.length -= 1
            return

        raise IndexError("Index out of range")
