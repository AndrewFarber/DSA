# Given an array, the task is to return every
# other element of the array starting from the first element.
# See: https://www.geeksforgeeks.org/print-alternate-elements-of-an-array/#recursive-approach


def alternate(lst: list[int]) -> list[int]:
    """
    Given an array, return a list containing
    every other element starting from the first element.
    """
    return [lst[i * 2] for i in range((len(lst) + 1) // 2)]


assert alternate([10, 20, 30, 40, 50]) == [10, 30, 50]
assert alternate([10, 20, 30, 40]) == [10, 30]
assert alternate([10, 20]) == [10]
assert alternate([10]) == [10]
assert alternate([]) == []
