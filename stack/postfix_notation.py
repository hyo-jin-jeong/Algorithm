def stack_fun(postfix):
    stack = []
    for s in postfix:
        if s.isdecimal():
            stack.append(int(s))
        else:
            first = stack.pop()
            seconde = stack.pop() 
            if s == '+':
                stack.append(seconde+first)
            elif s == '-':
                stack.append(seconde-first)
            elif s == '*':
                stack.append(seconde*first)
            elif s == '/':
                stack.append(seconde/first)  
    return stack[0]     

print(stack_fun('352+*9-'))