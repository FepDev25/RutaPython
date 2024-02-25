try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write("Titulo\n")
except Exception as e:
    print(e)
finally:
    archivo.close()

try:
    archivo = open('prueba.txt', 'a', encoding='utf8')
    archivo.write("Este es el texto del archivo\n")
    archivo.write("Nueva linea\n")
except Exception as e:
    print(e)
finally:
    archivo.close()

try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    print(archivo.readlines()[1])
except Exception as e:
    print(e)
finally:
    archivo.close()

try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
