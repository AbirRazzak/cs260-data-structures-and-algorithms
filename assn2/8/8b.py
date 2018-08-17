#!/usr/bin/env/python3
import sys

def evaluate_postfix(postfix):
    """
    Evaluates a postfix expression. Precondition: postfix is a valid postfix expression (no extra numbers, extra operators, etc.)
    :param postfix: Postfix expression to be evaluated
    :return: Result of the postfix expression, or error if unsupported operators used
    """
    stack = []
    postfix_tokens = postfix.split()

    for token in postfix_tokens:
        if token in "1234567890":
            stack.append(int(token)) # If number, push to stack
        else:
            num2 = stack.pop() # If operator then pop last
            num1 = stack.pop() # two numbers in stack

            # Do the calculation
            if token is "*":
                result = num1 * num2

            elif token is "/":
                result = num1 / num2

            elif token is "+":
                result = num1 + num2

            elif token is "-":
                result = num1 - num2

            else:
                return "Invalid operator detected."

            stack.append(result) # Add calculation to stack

    return stack.pop() # Pop the last remaining number, which is the result.

def main():
    if len(sys.argv) == 2:
        print(evaluate_postfix(sys.argv[1]))
    else:
        print("Parameter Error: Please give a postfix expression as a parameter.")

if __name__ == '__main__': main()

