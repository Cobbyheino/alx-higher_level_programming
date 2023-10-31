#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_Num = number % -10
elif number >= 0:
    last_Num = number % 10
if last_Num > 5:
    print(f"Last digit of {number} is {last_Num} and is greater than 5")
elif last_Num == 0:
    print(f"Last digit of {number} is {last_Num} and is 0")
else:
    print(f"Last digit of {number} is {last_Num} and is less than 6 and not 0")
