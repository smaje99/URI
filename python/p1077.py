"""Beecrowd exercise 1077.

See: https://judge.beecrowd.com/es/problems/view/1077
"""

priority: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def remove_brackets(stack: list[str]) -> str:
    parts: list[str] = []

    while stack and stack[-1] != "(":
        parts.append(stack.pop())

    return "".join(parts[::-1])


def postfixed(infix: str) -> str:
    _postfixed: list[str] = []
    _stack: list[str] = []
    for element in infix:
        if element.isalnum():
            _postfixed.append(element)
        elif element in priority:
            while _stack and priority[element] <= priority.get(_stack[-1], 0):
                _postfixed.append(_stack.pop())
            _stack.append(element)
        elif element == ")":
            _postfixed.append(remove_brackets(_stack))
        else:
            _stack.append(element)
    return "".join(_postfixed + _stack[::-1])


if __name__ == "__main__":
    n = int(input())
    if n > 0:
        for _ in range(n):
            equation = input()
            print(postfixed(equation))
