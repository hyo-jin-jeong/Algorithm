def stack(num, m):
    num = str(num)
    stack = []
    for x in num:
        while stack and m>0 and stack[-1]<x:
            stack.pop()
            m -= 1
        stack.append(x)
    if m!=0:
        stack = stack[:-m]
    return ''.join(map(str, stack))
print(stack(12345, 2))