# See README.md for instructions on what to do this program

import random

#random seed generates a set of numbers, based on the seed. these will always be the same outputs for a certain input.
#randint will draw from this set of numbers
random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)
