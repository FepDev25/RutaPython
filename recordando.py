"""*******************************Prints*******************************"""
print("Hola Mundo")
print("Me llamo Felipe")

"""*******************************Variables*******************************"""
nombre = "Felipe"
edad = 19
apellido = 'Peralta'
print(f"{nombre} {apellido}, y tiene {edad}")

l1, l2, l3 = 'Python','Java', "JavaScript"
print(l2) #Java
print(l1) #Python
print(l3) #JavaScript

print(type("Hola")) #<class 'str'>
print(type(edad)) #<class 'int'>
# print(edad + "10") Error
print(edad + 10) # 29
print("22" + '2') # 222

"""*******************************Operaciones Basicas*******************************"""
x = 10
y = -9
print(x + y) # 1
print(f"La suma de {2} + {4} es {2+4}") # La suma de 2 + 4 es 6