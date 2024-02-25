class Producto:
    contador_prodocutos = 0

    def __init__(self, nombre, precio):
        Producto.contador_prodocutos += 1
        self._id_producto = Producto.contador_prodocutos
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def id(self):
        return self._id_producto

    def __str__(self):
        return f"Producto = id:{self._id_producto}, nombre:{self._nombre}, precio:{self._precio}"


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    @property
    def id_orden(self):
        return self._id_orden

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, *productos):
        self._productos = productos

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_pago(self):
        total = 0
        for i in self._productos:
            total += float(i.precio)
        return total

    def __str__(self):
        producto_str = ''
        for i in self._productos:
            producto_str += i.__str__() + '|'
        return f"Orden = id:{self._id_orden}, productos: {producto_str}"

    def mostrar_orden(self):
        pago = self.calcular_pago()
        return f"El total a pagar es {pago}"
