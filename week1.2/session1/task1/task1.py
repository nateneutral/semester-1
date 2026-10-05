# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
index = shopping.index("bananas")
print(index)
shopping.pop(index)
shopping.insert(index,"grapes")

# Add yoghurt, just after milk
shopping.insert(shopping.index("milk")+1,"yoghurt")

print(shopping)