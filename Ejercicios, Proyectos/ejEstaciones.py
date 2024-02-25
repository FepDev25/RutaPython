mes = int(input("Ingrese el mes del año: "))
estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = "invierno."
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "primavera."
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "verano."
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "otonio."

print(f"Para el mes {mes }, la estacion es {estacion}")