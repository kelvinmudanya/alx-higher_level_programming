#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastDigit = number % 10

if number < 0:
    lastDigit = abs(number) % 10  # absolute value first for negative nums
    lastDigit = -lastDigit
else:
    lastDigit = number % 10

print("Last digit of", number, "is", lastDigit, "and is", end=" ")
if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
elif lastDigit < 6:
    print("less than 6 and not 0")
