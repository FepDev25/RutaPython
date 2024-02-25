class Persona: # Definicion de la clase (Mayuscula)
    def __init__(self, nombre, apellido, edad): # Metodo de inicializacion o metodoconstructor
        self._nombre = nombre # Se asignan directamente los atributos de la clase
        self._apellido = apellido
        self._edad = edad
    # Self: Metodo de instancia, va asociado con la clase

    # Encapsulamiento: Atributos privados, para acceder a ellos se crean los metodos get y set.
    @property # Getter
    def nombre(self):
        return self._nombre

    @nombre.setter # Setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self): # Metodo
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")

    def __str__(self): # Metodo String
        return f"Persona: {self._nombre} {self._apellido} {self._edad}"
    

# Realiza la prueba solo si ejecutamos dentro del archivo
if __name__ == "__main__":
    persona1 = Persona("Felipe", "Peralta", 18) # Crear un objeto de esa clase
    persona1.nombre = 'Diego Felipe' # Cambiar valores (setter)
    persona1.apellido = 'Peralta Peralta'
    persona1.edad = 22
    persona1.mostrar_detalle() # Acceder a un metodo

    # Crear atributos de un objeto en especifico
    persona1.telefono = 2875755 # Dinamismo, donde solo persona1 tiene este atributo. Variables al 'vuelo'

    del persona1 # Liberar recursos, eliminar objeto
