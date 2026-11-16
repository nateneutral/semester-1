import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
newnames = []
# Ask user to enter a number, then randomly choose that many names
nameNum = int(input("enter number of random names:"))
# from the list, avoiding any duplicate choices
for i in range(nameNum):
    r = random.randint(0, len(names)-1)
    newnames.append(names[r])
    names.pop(r)
# Display the chosen names, one per line
for i in newnames:
    print(i)