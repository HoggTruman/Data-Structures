# python3

from collections import namedtuple

Char = namedtuple("Char", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append((i, char))
            continue

        if char in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1][1], char):
                return i+1
            else:
                opening_brackets_stack.pop(-1)

    if opening_brackets_stack:
        return opening_brackets_stack[0][0] + 1
    else:
        return "Success"



def main():
    text = input()
    mismatch = print(find_mismatch(text))


if __name__ == "__main__":
    main()
