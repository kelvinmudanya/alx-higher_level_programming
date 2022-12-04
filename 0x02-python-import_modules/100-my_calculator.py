#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    operator = '+', '-', '*', '/'
    if len(argv) is not 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == '+':
            print(a, operator, b, "=", add(a, b))
        elif operator == '-':
            print(a, operator, b, "=", sub(a, b))
        elif operator == '*':
            print(a, operator, b, "=", mul(a, b))
        elif operator == '/':
            print(a, operator, b, "=", div(a, b))
