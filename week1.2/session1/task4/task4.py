# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here? I predict that the printed result will be tomato

both = fruit.intersection(vegetables)
print(both)

# Why does the following code display five items? it displays the combined items in both 
# sets fruit and vegetables, however sets only contain unique items.

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("Pineapple")
# Remove an item from vegetables
vegetables.remove("tomato")
# Find and display symmetric difference of the two sets
symDiff = fruit.symmetric_difference(vegetables)
print(symDiff)