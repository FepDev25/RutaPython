# Index para manipular Strings:

mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

resultado = mi_texto[9]
print(resultado)

resultado = mi_texto[-3]
print(resultado)

resultado = mi_texto.index("E")
print(resultado)

resultado = mi_texto.index("e")
print(resultado)

resultado = mi_texto.index("prueba")
print(resultado)

mi_texto = "Hola,esta es una frase"
resultado = mi_texto.index("e",9)
print(resultado)

resultado = mi_texto.index("e",16,22)
print(resultado)

resultado = mi_texto.rindex("e")
print(resultado)