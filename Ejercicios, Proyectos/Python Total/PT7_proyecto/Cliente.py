from Persona import Persona


class Cliente(Persona):
    numero_de_cuenta = 100000

    def __init__(self, nombre, apellido, balance):
        super().__init__(nombre, apellido)
        Cliente.numero_de_cuenta += 1
        self._id_cuenta = Cliente.numero_de_cuenta
        self._balance = balance

    @property
    def id_cuenta(self):
        return self._id_cuenta

    @property
    def balance(self):
        return self._balance

    def depositar(self, valor):
        if valor > 0:
            self._balance += valor
            print("Deposito exitoso.")
        else:
            print("Su valor a depositar es incorrecto.")

    def retirar(self, valor):
        if self._balance >= valor:
            self._balance -= valor
            print("Retiro exitoso.")
        else:
            print("Su cuenta no tiene los suficientes fondos.")

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}. Numero de cuenta: {self.id_cuenta}. Balance: ${self.balance}"

