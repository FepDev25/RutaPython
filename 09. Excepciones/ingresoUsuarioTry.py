def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa un numero: "))
        except Exception as e:
            print(f"Valor invalido: {e}")
        else:
            print(f"Ingresaste el numero: {numero}")
            break


pedir_numero()