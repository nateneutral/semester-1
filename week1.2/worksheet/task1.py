# Worksheet 1.2: Task 1 Solution
import sys
result = "Fail"
grade = input("please enter your grade 0-100")
if not(grade.isdecimal()):
    sys.exit("Grade must be an integer between 0 and 100")
else:
    grade = int(grade)
    
if grade < 0 or grade >100:
   sys.exit(" Grade must be an integer between 0 and 100")
if grade > 39:
    if grade > 69:
        result = "Distinction"
    else:
        result = "Pass"
print(f"{grade} is a {result}")
