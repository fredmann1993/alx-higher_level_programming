#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
def calculator():
    args = len(sys.argv[1:])
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] == "+":
            add(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == "-":
            sub(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == "/":
            div(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == "*":
            mul(int(sys.argv[1]), int(sys.argv[3]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
if _name_ == "_main_":
