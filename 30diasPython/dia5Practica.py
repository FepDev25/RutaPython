#Ejercicios: Nivel 1
#Declarar una lista vacía
lista = []

#Declarar una lista con más de 5 elementos
lista = ['Juancho', 'Mikey', 'Bruno', 'Polita', 'Perla']

#  Encuentra la longitud de tu lista
print(len(lista))

#Obtenga el primer elemento, el elemento del medio y el último elemento de la lista
print(lista[0])
print(lista[2])
print(lista[len(lista) - 1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Felipe', 18, 74, 'Singer', 'Your heart']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[len(lista) - 1])

# Print the list after modifying one of the companies
it_companies[-3] = 'Nintendo'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Uber')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Udemy')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
result = '#;  '.join(it_companies)
print(result)

# Check if a certain company exists in the it_companies list.
exists = 'Uber' in it_companies
print(exists)

# Sort the list using sort() method
print(f'Lista desordenada = {it_companies}')
it_companies.sort()
print(f'Lista ordenada = {it_companies}')

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(f'Lista invertida = {it_companies}')

# Slice out the first 3 companies from the list
del it_companies[:3]
print(it_companies)
 
# Slice out the last 3 companies from the list
del it_companies[-3:]
print(it_companies)

# Slice out the middle IT company or companies from the list
del it_companies[1]
print(it_companies)

"""
Remove the first IT company from the list
Remove the middle IT company or companies from the list
Remove the last IT company from the list
Remove all IT companies from the list
"""
it_companies.pop(0)
print(it_companies)
it_companies.pop()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
super_list = front_end + back_end
print(super_list)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL 
# after Redux.
full_stack = super_list
full_stack.insert(4, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]
print(ages, min, max)

# Add the min age and the max age again to the list
ages.append(min)
ages.append(max)

# Find the median age (one middle item or two middle items divided by two)
middle = ages[int(len(ages)/2)]
print(middle)

# Find the average age (sum of all items divided by their number )
suma = 0
print(ages)
for i in ages:
    suma += i
promedio = suma / len(ages)
print(suma, len(ages), promedio)

# Find the range of the ages (max minus min)
ages.sort()
range = ages[-1] - ages[0]
print(range)

# Compare the value of (min - average) and (max - average), use abs() method
print(ages)
c1 = abs(ages[0] - promedio)
c2 = abs(ages[-1] - promedio)
print(c1)
print(c2)

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle =countries[int(len(countries)/2)]
print(middle)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
lista1 = countries[:4]
lista2 = countries[4:]
print(lista1, lista2)

# Unpack the first three countries and the rest as scandic countries.
other = countries[:3]
print(other)
scandic = countries[3:]
print(scandic)
