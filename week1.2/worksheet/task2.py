# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()
numbers.sort()
print(numbers)

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {sum(numbers)/len(numbers)}")
print(f"Median = {numbers[len(numbers)//2]}")