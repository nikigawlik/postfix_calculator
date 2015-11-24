import ast

def binomial(n, k):
    if not(type(n) is int and type(k) is int):
        raise ValueError('expected int')
    res = 1
    for i in range(n-k+1,n+1):
        res *= i
    for i in range(1,k+1):
        res /= i
    return res

stack = [];

while 1:
    input = raw_input("")
    try:
        if input == "quit":
            break
        if input == "":
            pass
        elif input == "+":
            stack.append(stack.pop() + stack.pop())
        elif input == "-":
            stack.append(stack.pop() - stack.pop())
        elif input == "*":
            stack.append(stack.pop() * stack.pop())
        elif input == "/":
            stack.append(stack.pop() / stack.pop())
        elif input == "**":
            stack.append(stack.pop() ** stack.pop())
        elif input == "c" or input == "binomial":
            stack.append(binomial(int(stack.pop()), int(stack.pop())))
        elif input == "swap":
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif input == "reverse":
            stack.reverse()
        elif input == "rem" or input == "remove":
            stack.pop()
        elif input == "clear":
            stack = []
        else:
            try:
                stack.append(float(input))
            except (ValueError):
                try:
                    lit = ast.literal_eval(input)
                    if not isinstance(lit, list):
                        raise ValueError
                    for i in range(0,len(lit)):
                        lit[i] = float(lit[i])
                    stack = lit
                except (ValueError, SyntaxError):
                    print "could not parse '" + input + "'."
    except IndexError:
        print "Cannot execute operation: stack is empty."
    
    print stack
