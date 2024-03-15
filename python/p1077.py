priority = {'+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3}


def remove_brackets(stack):
    n = ''
    while stack:
        expression = stack.pop()
        if expression != '(':
            n += expression
        else:
            return n


def postfixed(infix):
    _postfixed = ''
    _stack = []
    for element in infix:
        if element.isalnum():
            _postfixed += element
        elif element in '+-*/^':
            priority_element = priority.get(element)
            while _stack and priority_element <= priority.get(_stack[-1], 0):
                _postfixed += _stack.pop()
            _stack.append(element)
        elif element == ')':
            _postfixed += remove_brackets(_stack)
        else:
            _stack.append(element)
    return _postfixed + ''.join(_stack[::-1])


if __name__ == '__main__':
    n = int(input())
    if n > 0:
        equations = []
        for _ in range(n):
            equations.append(input())
        for equation in equations:
            print(postfixed(equation))
