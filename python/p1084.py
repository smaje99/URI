while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    else:
        stack = []
        t = n - d
        numbers = map(int, input())
        for i, current in enumerate(numbers):
            while stack and len(stack) + n - i > t and stack[-1] < current:
                stack.pop()
            if len(stack) < t:
                stack.append(current)
        print(''.join(map(str, stack)))

