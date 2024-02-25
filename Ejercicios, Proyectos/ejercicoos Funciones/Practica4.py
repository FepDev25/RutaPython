def mostrar_primos(num):
    contador_primos = 0
    primos = []
    if num < 2:
        return 0
    for i in range(2, num+1):
        contador = 0
        for j in range(1, i+1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            primos.append(i)
            contador_primos += 1
    print(primos)
    return contador_primos

num = 50
prueba = mostrar_primos(num)
print(f'La cantidad de primos desde 2 hasta {num} es: {prueba}')
