from random import *
print("Bienvenido!")
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}. Vas a tener que adivinar un numero del 1 al 100." )

respuesta = randint(0, 101)

vidas = 1
while vidas <= 8:
    numero = int(input("Ingresa el numero: "))
    if numero < 0 or numero > 100:
        print("Numero invalido.")
        vidas += 1
    elif numero == respuesta:
        print(f"Felicidades {nombre}! Ganaste")
        print(f"Lo lograste despues de {vidas} intentos.")
        break
    elif numero > respuesta:
        print("El numero es menor al que ingresaste! Intentalo otra vez.")
        vidas += 1
    elif numero < respuesta:
        print("El numero es mayor al que ingresaste! Intentalo otra vez.")
        vidas += 1

if vidas == 9:
    print(f"Lo siento {nombre}, perdiste! El numero era {respuesta}")