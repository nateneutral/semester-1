# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()
numbers.sort()
print(numbers)

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {sum(numbers)/len(numbers)}")
if (len(numbers)%2) == 0 :
    num1 = numbers[len(numbers)//2]
    num0 = numbers[(len(numbers)//2)-1]
    Median = (num1 +num0)/2
    print(Median)
else:
    print(f"Median = {numbers[len(numbers)//2]}")