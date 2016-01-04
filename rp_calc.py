#!/usr/bin/python3.5

import ast
from decimal import Decimal, Context
import decimal

def binomial(n, k):
    if not(type(n) is int and type(k) is int):
        raise ValueError('expected int')
    res = 1
    for i in range(n-k+1,n+1):
        res *= i
    for i in range(1,k+1):
        res /= i
    return res

context = Context()

stack = [];
display_format = 'd'

while 1:
    input_str = input("")
    try:
        if input_str == "quit":
            break
        if input_str == "":
            pass
        elif input_str == "%" or input_str == "mod":
            stack.append(stack.pop() % stack.pop())
        elif input_str == "+":
            stack.append(stack.pop() + stack.pop())
        elif input_str == "-":
            stack.append(stack.pop() - stack.pop())
        elif input_str == "*":
            stack.append(stack.pop() * stack.pop())
        elif input_str == "/":
            stack.append(stack.pop() / stack.pop())
        elif input_str == "**":
            stack.append(stack.pop() ** stack.pop())
        elif input_str == "c" or input_str == "binomial":
            if (stack[-1] % 1 > 0.000000001) or (stack[-2] % 1 > 0.000000001):
                raise ValueError("expected something more int-like")
            #print(str(int(stack.pop())) + str(int(stack.pop())))
            stack.append(Decimal(binomial(int(stack.pop()), int(stack.pop()))))
        elif input_str == "swap":
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif input_str == "round":
            stack.append(round(stack.pop()))
        elif input_str == "reverse":
            stack.reverse()
        elif input_str == "rem" or input_str == "remove":
            stack.pop()
        elif input_str == "clear":
            stack = []
        elif input_str == "bin":
            print(", ".join([(bin(int(i)) if (i % 1 == 0) else str(i)) for i in stack]))
        else:
            try:
                stack.append(Decimal(input_str))
            except (ValueError, decimal.InvalidOperation):
                try:
                    lit = ast.literal_eval(input_str)
                    if not isinstance(lit, list):
                        raise ValueError
                    for i in range(0,len(lit)):
                        lit[i] = Decimal(str(lit[i]))
                    stack = lit
                except (ValueError, SyntaxError):
                    print("could not parse '" + input_str + "'.")
    except IndexError:
        print("Cannot execute operation: stack is empty.")
    except ValueError as e:
        print("ValueError: " + e)
    
    #print([str('{0:'+display_format+'}').format(int(i)) for i in stack])
    print('[' + ', '.join([context.to_sci_string(s) for s in stack]) + ']')

