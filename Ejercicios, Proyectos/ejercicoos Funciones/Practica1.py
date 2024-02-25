

def devolver_distintos(num1, num2, num3):
    maximo = max(num1, num2, num3)
    minimo = min(num1, num2, num3)
    if num1 + num2 + num3 > 15:
        return maximo
    elif num1 + num2 + num3 < 10:
        return minimo
    else:
        lista = [num1, num2, num3]
        lista.remove(maximo)
        lista.remove(minimo)
        return lista[0]

valor = devolver_distintos(6,7,10)
print(valor)

valor = devolver_distintos(2,1,3)
print(valor)

valor = devolver_distintos(4,2,7)
print(valor)

valor = devolver_distintos(13,10,40)
print(valor)

valor = devolver_distintos(0,-1,2)
print(valor)

valor = devolver_distintos(2,3,7)
print(valor)
