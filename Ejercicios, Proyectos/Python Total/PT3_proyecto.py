print("Bienvenida a este analizador de texto!")
cadena = input("Ingrese una frase, palabra o lo que desees: ")
print("Ahora ingresa 3 letras para realizar el analisis:")
l1 = input("Ingresa letra 1: ").lower()
l2 = input("Ingresa letra 2: ").lower()
l3 = input("Ingresa letra 3: ").lower()

print("\n")
# Primer analisis:
print("CANTIDAD DE VECES QUE SE REPITEN LAS LETRAS INGRESADAS")
lista_cadena = list(cadena.lower())
l1_contador = lista_cadena.count(l1)
l2_contador = lista_cadena.count(l2)
l3_contador = lista_cadena.count(l3)
contadores = {l1: l1_contador, l2: l2_contador, l3: l3_contador}
for i in contadores:
    print(f"La letra {i} se repite {contadores[i]} veces.")

print("\n")
# Segundo analisis:
print("CANTIDAD DE PALABRAS EN TOTAL")
lista_sin_espacio = cadena.split()
print(f"La cantidad de palabras de la cadena ingresa es {len(lista_sin_espacio)}.")

print("\n")
# Tercer analisis:
print("PRIMER Y ULTIMA LETRA")
primer_letra = cadena[0]
ultima_letra = cadena[-1]
print(f"La primer letra es {primer_letra} y la ultima es {ultima_letra}.")

print("\n")
# Cuarto analisis:
print("TEXTO INVERTIDO:")
print(f"El texto invertido es: {cadena[::-1]}.")

print("\n")
# Quinto analisis:
print("PALABRA PYTHON")
python_bool = "python" in cadena.lower()
python = "si" if python_bool else "no"
print(f"La palabra python {python} se encuentra en la cadena.")
