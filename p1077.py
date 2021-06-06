def priority_expression(n):
    if n == '^':
        return 4
    elif n in ('*', '/'):
        return 2
    elif n in ('+', '-'):
        return 1
    else:
        return 5


def priority_stack(n):
    if n == '^':
        return 3
    elif n in ('*', '/'):
        return 2
    elif n in ('+', '-'):
        return 1
    else:
        return 0


def postfixed(infix):
    _postfixed = []
    _stack = []
    while infix:
        n = infix.pop(-1)
        if n.isalnum():
            _postfixed.append(n)
        elif not _stack:
            _stack.append(n)
        elif n == ')' and _stack:
            while _stack:
                n = _stack.pop()
                if n != '(':
                    _postfixed.append(n)
                else:
                    break
        elif priority_expression(n) <= priority_stack(_stack[-1]):
            _postfixed.append(_stack.pop())
            _stack.append(n)
        else:
            _stack.append(n)
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
        ecuations = []
        for _ in range(n):
            ecuations.append(input())
        for ecuation in ecuations:
            print(''.join(postfixed(list(ecuation)[::-1])))
