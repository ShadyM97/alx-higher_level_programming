#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdigit = number % 10
else:
    number = number * (-1)
    lastdigit = (number % 10) * -1
if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    outputstring = f"Last digit of {number} is {lastdigit}" \
         " and is less than 6 and not 0"
    print(outputstring)
else:
    print(f"Last digit of {number} is {lastdigit} and is 0")
