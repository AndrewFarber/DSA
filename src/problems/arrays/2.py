# Given an array of n integers, and an integer element x,
# find whether element x is present in the array. Return the
# index of the first occurrence of x in the array, or -1 if
# it doesn’t exist.
# See: https://www.geeksforgeeks.org/linear-search/


def search(array: list[int], key: int) -> int:
    """
    Given an array of n integers, and an integer element key,
    return the index of the first occurrence of key in the array,
    or -1 if it doesn't exit.
    """
    for i in range(len(array)):
        if key == array[i]:
            return i
    return -1

assert search([1, 2, 3, 4], 3) == 2
assert search([10, 8, 30, 4, 5], 5) == 4
assert search([10, 8, 30], 6) == -1

