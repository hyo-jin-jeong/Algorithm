def stack(str):
    stack =[]
    sum = 0
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        else:
            stack.pop()
            if str[i-1] == '(':
                sum += len(stack)
            else:
                sum += 1
    return sum
print(stack('((()()))'))


