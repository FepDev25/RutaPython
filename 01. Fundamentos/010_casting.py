# Casting: Conversion entre tipos
# Implicita: Python cambia el tipo de dato autamaticamente
num = 20
num2 = 30.5
print(type(num))
print(type(num2))
num = num + num2

print(type(num)) # num se transforma en float debido a que fue sumado con num2

# Explicita: El usuario interfiere para la conversion
num1 = 5.9
num2 = int(num1)
print(num2)
print(type(num2))

num1 = "7.5"
num2 = "10"

print(f"{float(num1) + int(num2)}")