from NumerosIdenticosException import NumerosIdenticosException

# Preparar y preestablecer codigo cuando surja un error

try:
    10 / 0
except Exception as e:
    print(f"Ocurrio un error: {e}")

try:
    10 / 0
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {e}")

try:
    lista = [1, 2]
    print(lista[5])
except Exception as e:
    print(f"Ocurrio un error: {e}")


resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    resultado = a/b
    """if a == b:
        raise NumerosIdenticosException('numeros identicos')"""
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {e}")
except TypeError as e:
    print(f"Ocurrio un error: {e}")
else:
    print("No se arrojo ninguna excepcion")
finally:
    print("EJECUCION FINAL")

print(f"Resultado: {resultado}")
print("Continuamos...")


