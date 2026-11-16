import random

# Get user to input how many random numbers they want
RandNum = int(input("Enter number of randoms: "))
# Generate this many random numbers
for i in range(RandNum): #RandNum loops, writing random numbers to rand.txt
    with open("random.txt", "a") as f:
        r = random.randint(1, 100)
        f.write(f"{r}\n")
# Write the random numbers to a file named random.txt, one number per line
