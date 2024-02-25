# Cumple la funcion deun condicional, pero con una mejor sintaxis 

serie = 'N-02'

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case _: # En caso de no umplir todas las condiciones anteriores
        print('No encontrado')

cliente = {'nombre': 'Felipe',
           'edad': 18,
           'ocupacion': "estudiante"}

pelicula = {'titulo': 'Matrix',
            'ficha': {'actor': 'Keanu Reeves',
                     'director': 'Lana y Lilly'}}

elementos = [cliente, pelicula, 'libro']

for i in elementos:
    match i:
        case {'nombre': nombre,
              'edad': edad,
             'ocupacion': ocupacion}:
            print("Esto es un cliente.")
            print(f"{nombre}, {edad}, {ocupacion}")
        case {'titulo': titulo,
            'ficha': {'actor': actor,
                     'director': director}}:
            print("Esto es una pelicula")
            print(f"{titulo}, {actor}, {director}")
        case _:
            print("No se que es esto")


def evaluar_expresion(expresion):
    match expresion:
        case 0:
            print("La expresión es cero")
        case 1:
            print("La expresión es uno")
        case _:
            print("La expresión es otra cosa")

evaluar_expresion(0)
evaluar_expresion(1)
evaluar_expresion(5)


punto = (3, 5)

match punto:
    case (0, 0):
        print("El punto está en el origen")
    case (x, 0):
        print(f"El punto está en el eje x en la posición {x}")
    case (0, y):
        print(f"El punto está en el eje y en la posición {y}")
    case (x, y):
        print(f"El punto está en la posición ({x}, {y})")
