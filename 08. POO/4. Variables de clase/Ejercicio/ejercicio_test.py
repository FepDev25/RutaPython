from Clases import Orden, Producto

producto1 = Producto("Leche", 2)
producto2 = Producto("Huevos", 4.5)
producto3 = Producto("Galletas", 2.5)
producto4 = Producto("Cola", 1.10)
producto5 = Producto("Pollo", 9.55)
producto6 = Producto("Azucar", 8)
print(producto1)
print(producto2)
print(producto3)
print(producto4)
print(producto5)
print(producto6)

orden1 = Orden([producto1, producto2, producto3, producto4, producto5])
print(orden1)
print(orden1.mostrar_orden())

orden2 = Orden([producto6, producto5])
orden2.agregar_producto(producto4)
print(orden2)
print(orden2.mostrar_orden())
