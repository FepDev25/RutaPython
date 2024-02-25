# Hace referencia a funciones que se llaman a si mismas para completar una tarea

def factorial_recursivo(num):
    if num == 1: # Punto de freno. Es necesario para reducir los errores
        return 1
    else:
        return num * factorial_recursivo(num - 1)

def factorial(num):
    resultado = 1
    for i in range(1, num+1):
        resultado = resultado * i
    return resultado

def imprimirRecursivo(num):
    if num >= 1:
        print(num)
        imprimirRecursivo(num - 1)
    elif num < 0:
        print("Valor incorrecto")

print(factorial_recursivo(5))
print(factorial(5))

imprimirRecursivo(6)
imprimirRecursivo(-2)