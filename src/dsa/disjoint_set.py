"""
This module provides an implementation for disjoint set.
"""

from collections.abc import Hashable
from typing import Set


class DisjointSet:
    def __init__(self, elements: Set) -> None:
        """
        Initialize the DisjointSet data structure with a set of elements.

        At initialization, each element will be in its own component.
        """
        self._index_map: dict[int, Hashable] = {}
        self._element_map: dict[Hashable, int] = {}
        self._array: list[int] = list()
        self._size: list[int] = list()

        for i, element in enumerate(elements):
            self._index_map[i] = element
            self._element_map[element] = i
            self._array.append(i)
            self._size.append(1)

    def _get_element(self, index: int) -> Hashable:
        if not (0 <= index < len(self._array)):
            raise IndexError("Index is out of bounds")
        return self._index_map[index]

    def _get_index(self, element: Hashable) -> int:
        if element not in self._element_map:
            raise ValueError("Element is not in the UnionFind set.")
        return self._element_map[element]

    def _union(self, i: int, j: int) -> None:
        irep = self._find(i)
        jrep = self._find(j)

        if irep == jrep:
            return

        isize = self._size[irep]
        jsize = self._size[jrep]
        if isize < jsize:
            self._array[irep] = jrep
            self._size[jrep] += isize
        else:
            self._array[jrep] = irep
            self._size[irep] += jsize

    def _find(self, i: int) -> int:
        irep = self._array[i]
        if i != irep:
            self._array[i] = self._find(irep)  # Path compression
        return irep

    def union(self, element_1: Hashable, element_2: Hashable) -> None:
        """
        Merge two components.
        """
        i = self._get_index(element_1)
        j = self._get_index(element_2)
        self._union(i, j)

    def find(self, element: Hashable) -> Hashable:
        """
        Find the representative component. Two elements are within the
        same component if they result in the same representative component.
        (e.g., find(x) == find(y)).
        """
        i = self._get_index(element)
        irep = self._find(i)
        return self._index_map[irep]


if __name__ == "__main__":
    elements = set(["A", "B", "C", "D"])
    uf = DisjointSet(elements)

    uf.union("A", "B")
    uf.union("B", "C")
    print("A and C are related:", uf.find("A") == uf.find("C"))
    print("A and D are related:", uf.find("A") == uf.find("D"))
