# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ["Luke", "Asher", "Levi", "Axel"]

print(f'This is the second student {students[1]}')
print(f'This is the last student {students[-1]}')

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "[food goes here] is a good food".

foods = ('chicken','bread','lettuce','tomato')
print(foods)

for food in foods:
    print(food)

# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods

for food in foods:
    print(foods[2:4])

for food in foods:
    last_two = slice(2,4)
    print(foods[last_two])
