import os
import sys

example_directory = os.path.dirname(__file__)
sys.path.append(os.path.dirname(example_directory))

from dsa.stacks import Stack


def valid_brackets(input: str) -> bool:
    """
    Returns True if the bracket string is valid
    (e.g., "({[]})[]") or False if the string
    is invalid (e.g., "{[)}").
    """
    brackets = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    stack = Stack()

    for char in input:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.size() == 0:
                return False
            open_bracket = stack.pop()
            if brackets[char] != open_bracket:
                return False
        else:
            continue
    return (stack.size() == 0)


if __name__ == "__main__":
    print("Running valid_brackets")
    print("({[]})[]({})", valid_brackets("({[]})[]({})"))
    print("Empty", valid_brackets(""))
    print("]", valid_brackets("]"))
    print("[", valid_brackets("["))
    print("]()", valid_brackets("]()"))
    print("()[", valid_brackets("()["))
    print("({[]})[()", valid_brackets("({[]})[()"))
    print("({[]})]()", valid_brackets("({[]})]()"))
