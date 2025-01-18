"""
This module provides an example implementation for a hash table
using the open addressing collision resolution technique. Since Python
already contains a hash table primitive (i.e., `dict`), the below code should
only be used for learning purposes.
"""

from __future__ import annotations
from typing import Hashable, Any


class TOMBSTONE:
    pass


TableEntry = tuple[Hashable, Any] | None | TOMBSTONE

tombstone = TOMBSTONE()


def get_hash(key: Hashable) -> int:
    """
    Returns a positive integer hash of a key.
    """
    return hash(key) & 0x7FFFFFFF


def get_initial_index(key: Hashable, n: int) -> int:
    """
    Returns the initial index of a key in a hash table
    of size n for use with a probing technique.
    """
    return get_hash(key) % n


def get_index(initial_index: int, x: int, n: int) -> int:
    """
    Returns the index of a key in a hash table.
    Uses linear probing.
    """
    return (initial_index + x) % n


class HashTable:
    def __init__(self) -> None:
        self.n_items = 0
        self.threshold = 0.65
        self.table: list[TableEntry] = [None] * 100

    @property
    def length(self) -> int:
        return len(self.table)

    @property
    def load(self) -> float:
        return self.n_items / self.length

    def _probe_limit(self) -> int:
        return int(self.length * 0.75)

    def _resize(self) -> None:
        if self.load > self.threshold:
            new_length = self.length * 2
            new_table: list[TableEntry] = [None] * new_length

            self.n_items = 0

            for element in self.table:
                if isinstance(element, tuple):
                    key, value = element
                    x = 0
                    initial_index = get_initial_index(key, new_length)
                    index = initial_index

                    while new_table[index] is not None:
                        index = get_index(initial_index, x, new_length)
                        x += 1

                    new_table[index] = (key, value)
                    self.n_items += 1

            self.table = new_table

    def set(self, key: Hashable, value: Any) -> None:
        """
        Add or update a element in the hash table
        with the specified `key` and `value`.
        """
        x = 1
        initial_index = get_initial_index(key, self.length)
        index = initial_index
        first_tombstone_index = None

        while self.table[index] is not None:
            k = self.table[index]

            if k is tombstone:
                if first_tombstone_index is None:
                    first_tombstone_index = index
            elif isinstance(k, tuple) and k[0] == key:
                self.table[index] = (key, value)
                return

            index = get_index(initial_index, x, self.length)
            x += 1

            if x > self._probe_limit():
                self._resize()
                self.set(key, value)
                return

        if first_tombstone_index is not None:
            self.table[first_tombstone_index] = (key, value)
        else:
            self.table[index] = (key, value)

        self.n_items += 1
        self._resize()

    def get(self, key: Hashable, default=None) -> Any:
        """
        Get an value from the hash table if it exists.
        Otherwise, returns the `default` value.
        """
        x = 1
        initial_index = get_initial_index(key, self.length)
        index = initial_index

        while self.table[index] is not None:
            k = self.table[index]

            if k is tombstone:
                index = get_index(initial_index, x, self.length)
                x += 1
            elif isinstance(k, tuple) and k[0] == key:
                return k[1]
            else:
                index = get_index(initial_index, x, self.length)
                x += 1

            if x > self._probe_limit():
                raise RuntimeError("Exceeded probe limit.")

        return default

    def remove(self, key: Hashable) -> None:
        """
        Remove a `key` from the hash table if it exists.
        """
        x = 1
        initial_index = get_initial_index(key, self.length)
        index = initial_index

        while self.table[index] is not None:
            k = self.table[index]
            if isinstance(k, tuple) and k[0] == key:
                self.table[index] = tombstone
                self.n_items -= 1
                return
            index = get_index(initial_index, x, self.length)
            x += 1

            if x > self._probe_limit():
                raise RuntimeError("Exceeded probe limit.")
