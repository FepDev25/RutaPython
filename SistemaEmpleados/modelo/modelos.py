class Persona:
    def __init__(self, nombre, edad, cedula):
        self._nombre = nombre
        self._edad = edad
        self._cedula = cedula
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def cedula(self):
        return self._cedula
    
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula
    
    def __str__(self) -> str:
        return f"Persona: (Nombre: {self._nombre}, Cedula: {self._cedula}, Edad: {self._edad})"
    

class Empleado(Persona):
    def __init__(self, nombre, edad, cedula, salario, cargo):
        super().__init__(nombre, edad, cedula)
        self._salario = salario;
        self._cargo = cargo;

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        if isinstance(salario, (int, float)) and salario >= 0:
            self._salario = salario
        else:
            print("Error: El salario debe ser un número positivo.")

    @property
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo
    
    def __str__(self) -> str:
        return f"Empleado: ({super().__str__()}, Salario: {self._salario}, Cargo: {self._cargo})"    