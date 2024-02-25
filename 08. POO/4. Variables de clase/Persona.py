class Persona:
    contador_personas = 0

    def __init__(self, nombre):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre

    def __str__(self):
        return f"Persona [id: {self.id_persona}, nombre: {self.nombre}]"



persona1 = Persona("Felipe")
persona2 = Persona("Juan")
print(persona1)
print(persona2)
print(f"Valor contador Personas: {Persona.contador_personas}")