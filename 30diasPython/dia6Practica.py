# Exercises: Level 1

# Create an empty tuple
empty_tuple = ()
print(type(empty_tuple))

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Karen', 'Maria Paz')
friends = ('Esteban', 'Juan')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + friends
print(siblings)

# How many siblings do you have?
print(f'I have {len(siblings)} siblings')

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Diego', 'Nube')
print(family_members)
print(type(family_members))

# Exercises: Level 2

# Unpack siblings and parents from family_members
parents = family_members[4:]
siblings = family_members[:4]
print(parents)
print(siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable 
# called food_stuff_tp.
fruits = ('Orange', 'Apple', 'Banana')
vegetables = ('Tomato', 'Onion', 'Potato')
animal = ('Chicken', 'Cow', 'Sheep')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice = food_stuff_lt[3:5]
print(slice)

# Slice out the first three items and the last three items from food_staff_lt list
slice = food_stuff_lt[:3]
print(slice)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
