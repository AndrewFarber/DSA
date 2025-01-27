"""
This module provides implementation for a Fenwick Tree.
"""

from __future__ import annotations


def LSB(i: int) -> int:
    """
    Compute the least significant bit (LSB) of the given integer.
    """
    return i & -i


class FenwickTree:
    """
    Implementation of a Fenwick Tree (Binary Indexed Tree) for efficient range queries
    and point updates on a list of integers.
    """

    def __init__(self, array: list[int]) -> None:
        """
        Initialize the Fenwick Tree with the given array.
        """
        N = len(array) + 1
        self.tree = [0] * N
        self.length = N
        for i in range(1, N):
            self.update(i, array[i - 1])  # Construct the tree.

    def prefix_sum(self, i: int) -> int:
        """
        Compute the prefix sum from the start of the array up to the given index.
        """
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= LSB(i)
        return result

    def range_query(self, i: int, j: int) -> int:
        """
        Compute the sum of elements in the range [i, j].
        """
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

    def update(self, i: int, x: int) -> None:
        """
        Update the value at index i by adding x to it.
        """
        if i <= 0 or i >= self.length:
            raise IndexError("Index out of bounds.")
        while i < self.length:
            self.tree[i] += x
            i += LSB(i)
