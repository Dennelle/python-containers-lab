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

foods = ('BLT','Mac and Cheese','Peanut Butter and Jelly','Grilled Cheese')
print(foods)

for food in foods:
    print(food)

# Exercise 3
# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods

for food in foods:
    print(foods[2:4])

for food in foods:
    last_two = slice(2,4)
    print(foods[last_two])

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city':'Linden',
    'country':'Guyana',
    'population':805000
}
print(f'I was born in {home_town["city"]}, {home_town["country"]} - population of {home_town["population"]}')

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

for item in home_town.items():
    print(item)

# Exercise 6
# Create an empty list named cohort.
# Using a for loop to iterate over the students list.
# Hint: Use the enumerate function to provide both the index & student
# Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:
# {
#    'student': 'Tina',
#    'fav_food': 'Cheeseburger'
#  }
# Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).
cohort = []

# for student in students:
#     print(student)

# new_students = enumerate(students)
# print(list(new_students))

# new_foods = enumerate(foods)
# print(list(new_foods))

# cohort.append(students)
# cohort.append(foods)

# print(cohort)

for i in range(len(students)):
    student_dict ={'student':students[i], 'fav_food':foods[i]}
    cohort.append(student_dict)

for item in cohort:
    print(item)


# Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.

# new_list = [expression for item in iterable if condition]

awesome_students = [f'{student} is awesome!' for student in students]
for awesome_student in awesome_students:
    print(awesome_students)




# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.
'''
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
[expression for item in iterable if condition]
'''

filter_food = [food for food in foods if 'a' in food.lower()]
for food in filter_food:
    print(food)
