#!/usr/bin/python3

import sys

def evaluate_prefix(prefix):
    stack = prefix.split()
    stack.reverse() # We are going to evaluate the prefix backwards

    # Convert all numbers into ints in prefix
    for i in range(len(stack)):
        if stack[i] in "1234567890":
            stack[i] = int(stack[i])

    while len(stack) != 1:
        i = 0
        for i in range(0, len(stack)):
            if isinstance(stack[i], str): # if the current token is a string, then it must be an operator
                break

        num2 = stack.pop(i-2) # Number 2 before it must be second number (because reversed)
        num1 = stack.pop(i-2) # Number that takes it's spot is first number
        op = stack.pop(i-2)   # Last thing in that index is the operator itself

        if op is "*":
            result = num1 * num2
        elif op is "/":
            result = num1 / num2
        elif op is "+":
            result = num1 + num2
        elif op is "-":
            result = num1 - num2
        else:
            return "Invalid operator used."

        stack.insert(i-2, result)

    return stack.pop() # Last number left is the answer

def main():
    if len(sys.argv) == 2:
        print(evaluate_prefix(sys.argv[1]))
    else:
        print("Parameter Error: Please pass a prefix expression as a parameter")

if __name__ == '__main__': main()
