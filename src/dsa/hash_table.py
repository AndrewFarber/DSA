"""
This module provides an example implementation for a hash table. Since Python
already contains a hash table primitive (i.e., `dict`), the below code should
only be used for learning purposes.
"""

from __future__ import annotations
from typing import Hashable, Any


def get_hash(key: Hashable) -> int:
    """
    Returns the non-negative hash of a key.
    """
    return abs(hash(key))


def get_index(key: Hashable, n: int) -> int:
    """
    Returns the index of a key for a hash table
    of length n.
    """
    return get_hash(key) % n


class Node:
    def __init__(
        self,
        key: Hashable,
        value: Any,
        next: Node | None = None,
    ) -> None:
        self.key: Hashable = key
        self.hash: int = get_hash(key)
        self.value: Any = value
        self.next: Node | None = next

    def equal(self, key: Hashable) -> bool:
        if self.hash == get_hash(key):
            if self.key == key:
                return True
        return False


class LinkedList:
    def __init__(self) -> None:
        self._length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    @property
    def length(self):
        """
        The number of nodes in the list.
        """
        return self._length

    @property
    def hash(self) -> int | None:
        """
        The hashes of every node in the list.
        """
        if self.head:
            return self.head.hash
        return None

    def _search(self, key: Hashable) -> tuple[Node | None, Node | None]:
        """
        Searches the list for the specified key and returns
        the previous and matching node if they exist.
        The nodes are returned in a tuple: (previous, matching)
        """
        previous = None
        current = self.head
        while current is not None:
            if current.equal(key):
                return (previous, current)
            previous = current
            current = current.next
        return (None, None)

    def get(self, key: Hashable) -> Node | None:
        """
        Get a node from the list matching the specified key.
        """
        _, matched = self._search(key)
        return matched

    def insert(self, key: Hashable, value: Any) -> None:
        """
        Inserts a key at the head of the list.
        """
        if self._length == 0:
            n = Node(key, value)
            self.head = n
            self.tail = n
            self._length += 1
        else:
            h = self.head
            self.head = Node(key, value, next=h)
            self._length += 1

    def remove(self, key: Hashable) -> None:
        """
        Remove a key from the list.
        """
        previous, removed = self._search(key)
        if removed is None:
            return None

        if self._length == 1:
            self.head = None
            self.tail = None
            self._length -= 1
            return None

        if removed == self.head:
            self.head = removed.next
            self._length -= 1
            return None

        if removed == self.tail:
            assert previous is not None
            previous.next = None
            self.tail = previous
            self._length -= 1
            return None

        assert previous is not None
        previous.next = removed.next
        self._length -= 1
        return None


class HashTable:
    def __init__(self) -> None:
        self.size = 0
        self.threshold = 0.75
        self.lst: list[LinkedList | None] = [None] * 100

    @property
    def length(self) -> int:
        return len(self.lst)

    def _resize(self) -> None:
        if (self.size + 0.0) / self.length > self.threshold:
            new_length = self.length * 2
            new_lst: list[LinkedList | None] = [None] * new_length
            for i in range(self.length):
                ll = self.lst[i]
                if ll is not None:
                    # Must resize entire table (not just node)
                    # since new hash collisions are possible with
                    # new length
                    current = ll.head
                    while current is not None:
                        index = get_index(current.key, new_length)
                        ll = new_lst[index]
                        if ll is None:
                            ll = LinkedList()
                            new_lst[index] = ll
                        ll.insert(current.key, current.value)
                        current = current.next
            self.lst = new_lst

    def set(self, key: Hashable, value: Any) -> None:
        index = get_index(key, self.length)
        ll = self.lst[index]
        if ll is None:
            ll = LinkedList()
            ll.insert(key, value)
            self.lst[index] = ll
            self.size += 1
            self._resize()
        else:
            print("Collision @", index, "with key", key)
            node = ll.get(key)
            if node is None:
                ll.insert(key, value)
            else:
                node.value = value

    def get(self, key: Hashable, default=None) -> Any:
        index = get_index(key, self.length)
        ll = self.lst[index]
        if ll is None:
            return default
        else:
            node = ll.get(key)
            if node is None:
                return default
            return node.value

    def remove(self, key: Hashable) -> None:
        index = get_index(key, self.length)
        ll = self.lst[index]
        if ll is not None:
            ll.remove(key)
            if ll._length == 0:
                self.size -= 1
                self.lst[index] = None
        return None
