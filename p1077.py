priority_expression = {'+': 1,
                       '-': 1,
                       '*': 2,
                       '/': 2,
                       '^': 4}

priority_stack = {'+': 1,
                  '-': 1,
                  '*': 2,
                  '/': 2,
                  '^': 3}


def remove_brackets(stack):
    while stack:
        expression = stack.pop()
        if expression != '(':
            yield expression
        else:
            break


def postfixed(infix):
    _postfixed = []
    _stack = []
    p_expression = None
    p_stack = None
    for element in infix:
        if not element.isalnum() and _stack:
            p_expression = priority_expression.get(element, 5)
            p_stack = priority_stack.get(_stack[-1], 0)

        if element.isalnum():
            _postfixed.append(element)
        elif not _stack:
            _stack.append(element)
        elif element == ')' and _stack:
            _postfixed.extend(remove_brackets(_stack))
        elif p_expression == p_stack:
            _postfixed.append(_stack.pop())
            _stack.append(element)
        elif p_expression < p_stack:
            _postfixed.extend(_stack[::-1])
            _stack.clear()
            while '(' in _postfixed:
                _postfixed.remove('(')
            _stack.append(element)
        else:
            _stack.append(element)
    while _stack:
        _postfixed.append(_stack.pop())
    return _postfixed


if __name__ == '__main__':
    '''3
    A*2
    (A*2+c-d)/2
    (2*4/a^b)/(2*c)
    '''
    n = int(input())
    if 0 < n < 1000:
        equations = []
        for _ in range(n):
            equations.append(input())
        for equation in equations:
            print(''.join(postfixed(equation)))
