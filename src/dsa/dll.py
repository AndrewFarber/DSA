"""
This module provides an implementation for a doubly linked lists.
"""

from __future__ import annotations
from typing import Any


class InconsistentState(Exception):
    pass


class EmptyList(Exception):
    pass


class OutOfBounds(Exception):
    pass


class Node:
    def __init__(
        self,
        data: Any,
        prev: Node | None = None,
        next: Node | None = None,
    ) -> None:
        """
        Instantiate a node with data.
        Optionally point to a previous or next node.
        """
        self.data: Any = data
        self.prev: Node | None = prev
        self.next: Node | None = next

    def __repr__(self) -> str:
        return f"<Node(data={self.data})>"


class LinkedList:
    """
    A linked list is a linear collection of nodes that
    hold data and point to other nodes.
    """

    def __init__(self) -> None:
        """
        Instantiate a linked list containing no nodes.
        """
        self._length: int = 0
        self._head: Node | None = None
        self._tail: Node | None = None

    @property
    def length(self) -> int:
        """
        The number of nodes in the linked list.
        """
        return self._length

    @property
    def head(self) -> Node | None:
        """
        The first node in the linked list.
        """
        return self._head

    @property
    def tail(self) -> Node | None:
        """
        The last node in the linked list.
        """
        return self._tail

    def insert(self, position: int, data: Any) -> Node:
        """
        Insert a node with the provided data at the specified position.
        Returns the new node.

        If the provided position matches the length of the list, a new node
        will be appended to the end.
        """
        # Insert first node
        if position == 0 and self._length == 0:
            n = Node(data)
            self._head = n
            self._tail = n
            self._length += 1
            return n

        # Insert at head
        if position == 0:
            after = self._head
            assert after is not None  # Inconsistent state
            new = Node(data, next=after)
            after.prev = new
            self._head = new
            self._length += 1
            return self._head

        # Insert at tail (i.e., Append)
        if position == self._length:
            before = self._tail
            assert before is not None  # Inconsistent state
            new = Node(data, prev=before)
            before.next = new
            self._tail = new
            self._length += 1
            return self._tail

        # Insert in middle
        if 0 < position < self._length:
            before = self.traverse(position - 1)
            after = before.next
            assert after is not None  # Inconsistent state
            new = Node(data, prev=before, next=after)
            before.next = new
            after.prev = new
            self._length += 1
            return new

        raise OutOfBounds

    def remove(self, position: int) -> Any:
        """
        Remove the node at the specified position.
        Returns the data contained in the removed node.
        """
        if self._length == 0 and self._head is None and self._tail is None:
            raise EmptyList
        if self._head is None or self._tail is None:
            raise InconsistentState

        # Remove only node
        if position == 0 and self._length == 1:
            removed = self._head
            self._head = None
            self._tail = None
            self._length -= 1
            return removed.data

        # Remove at head
        if position == 0:
            removed = self._head
            after = self._head.next
            assert after is not None
            self._head = after
            self._head.prev = None
            self._length -= 1
            return removed.data

        # Remove at tail
        if position == (self._length - 1):
            removed = self._tail
            before = self.traverse(self._length - 2)
            assert before is not None  # Inconsistent state
            before.next = None
            self._tail = before
            self._length -= 1
            return removed.data

        # Remove in middle
        if 0 < position < self._length - 1:
            before = self.traverse(position - 1)
            assert before.next is not None  # Inconsistent state
            removed = before.next
            after = removed.next
            assert after is not None  # Inconsistent state
            before.next = after
            after.prev = before
            self._length -= 1
            return removed.data

        raise OutOfBounds

    def traverse(self, position: int) -> Node:
        """
        Get the node at the specified position.

        For a linked list containing n nodes, the first
        node in the linked list is at position zero
        and the last node in the linked list is at
        position n-1.
        """
        if self._length == 0 and self._head is None and self._tail is None:
            raise EmptyList
        if not (0 <= position < self._length):
            raise OutOfBounds
        if self._head is None or self._tail is None:
            raise InconsistentState

        node: Node | None = None
        if position == 0:
            return self._head
        elif position == self._length - 1:
            return self._tail
        elif position <= self._length // 2:
            node = self._head
            for _ in range(position):
                assert node is not None  # Inconsistent state
                node = node.next
        else:
            node = self._tail
            for _ in range(self._length - 1, position, -1):
                assert node is not None  # Inconsistent state
                node = node.next

        assert node is not None  # Inconsistent state
        return node
