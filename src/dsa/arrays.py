"""
This module provides example implementations for static and dynamic arrays. Since Python
already contains a dynamic array primitive (i.e., `list`), the below code should
only be used for learning purposes.
"""

from typing import Any


class StaticArray:
    """
    Fixed length container containing n elements indexable
    from range [0, n-1].
    """

    def __init__(self, length: int) -> None:
        """
        Instantiate a static array of the specified `length`.
        """

        if length <= 0:
            raise ValueError("length must be greater than zero")

        self.array: list = [None] * length
        self.length: int = length

    def size(self) -> int:
        """
        Returns the length of the array.
        """
        return self.length

    def clear(self) -> None:
        """
        Replaces all elements of the array with `None` values.
        """
        for i in range(self.length):
            self.array[i] = None

    def get(self, index: int) -> Any:
        """
        Return the element in the array at the specified `index`.
        """
        if 0 <= index <= (self.length - 1):
            return self.array[index]
        else:
            raise IndexError

    def set(self, index: int, value: Any) -> None:
        """
        Set the element in the array at the specified `index`.
        """
        if 0 <= index <= (self.length - 1):
            self.array[index] = value
        else:
            raise IndexError

    def contains(self, value: Any) -> bool:
        """
        Returns true if the array contains the specified `value`.
        """
        for i in range(self.length):
            if self.array[i] == value:
                return True
        return False


class DynamicArray:
    """
    A dynamic length container containing n elements indexable
    from range [0, n-1].
    """

    def __init__(self, length: int) -> None:
        """
        Instantiate a dynamic array of the specified `length`.
        """
        self.array = StaticArray(length)

    def size(self) -> int:
        """
        Returns the length of the array.
        """
        return self.array.size()

    def clear(self) -> None:
        """
        Replaces all elements of the array with `None` values.
        """
        self.array.clear()

    def get(self, index: int) -> Any:
        """
        Return the element in the array at the specified `index`.
        """
        return self.array.get(index)

    def set(self, index: int, value: Any) -> None:
        """
        Set the element in the array at the specified `index`.
        """
        self.array.set(index, value)

    def contains(self, value: Any) -> bool:
        """
        Returns true if the array contains the specified `value`.
        """
        return self.array.contains(value)

    def insert(self, value: Any) -> None:
        """
        Inserts a new value at the beginning of the array.
        All other elements are shifted.
        """
        new_length = self.array.size() + 1
        array = StaticArray(new_length)
        array.set(0, value)
        for i in range(self.array.size()):
            array.set(i + 1, self.array.get(i))
        self.array = array

    def append(self, value: Any) -> None:
        """
        Inserts a new value at the end of the array.
        All other elements are shifted.
        """
        new_length = self.array.size() + 1
        array = StaticArray(new_length)
        for i in range(self.array.size()):
            array.set(i, self.array.get(i))
        array.set(new_length - 1, value)
        self.array = array

    def delete(self, index: int) -> None:
        """
        Removes the element at the specified `index`.
        All other elements are shifted.
        """
        new_length = self.array.size() - 1
        array = StaticArray(new_length)
        for i in range(self.array.size()):
            if i < index:
                array.set(i, self.array.get(i))
            elif i == index:
                pass
            elif i > index:
                array.set(i - 1, self.array.get(i))
        self.array = array
