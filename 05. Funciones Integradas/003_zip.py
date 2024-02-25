nombres = ['Ana', 'Hugo', 'Valeria']
edades = [18,71,32]
ciudades = ['Lima', 'Quita', 'Quito']
combinados = list(zip(nombres, edades, ciudades))
print(type(combinados[0]))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} vive en {ciudad} y tiene {edad}.")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for capital, pais in list(zip(capitales, paises)):
    print(f"La capital de {pais} es {capital}")