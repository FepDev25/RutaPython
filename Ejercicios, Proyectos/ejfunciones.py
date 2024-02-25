def convertir_celcius_a_fahrenheit(temperatura):
    return (temperatura * (9/5)) + 32

def convertir_fahrenheit_a_celcius(temperatura):
    return (temperatura - 32) * (5/9)


celcius = int(input("Ingrese su temperatura en celcius: "))
print(f"{celcius}C son {convertir_celcius_a_fahrenheit(celcius)}F")

fahrenheit = int(input("Ingrese su temperatura en fahrenheit: "))
print(f"{fahrenheit}F son {round(convertir_fahrenheit_a_celcius(fahrenheit), 2)}C")
