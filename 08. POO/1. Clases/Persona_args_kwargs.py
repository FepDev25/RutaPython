class Persona: 
    def __init__(self, nombre, apellido, edad, *tupla, **dic):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.mascotas = tupla
        self.habilidades = dic

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.edad} [{self.mascotas}] [{self.habilidades}]"


   
if __name__ == "__main__":
    habilidades = {'lenguajes': ['Python', 'Java', 'JavaScript'],
                   'matematicas': True}
    persona1 = Persona("Felipe", "Peralta", 18, *'Bruno', 'Polita', 'Perla', **habilidades) 
    print(persona1) 