from cliente import Cliente
class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo= saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            return True

    def extrato(self):
        print("numero: {} \ntitular: {} \nsaldo: {}".format(self['numero'], self['titular'], self['saldo']))

    def transferir(self, destino, valor):
        retirada = self.sacar(valor)
        if retirada == False:
            return False
        else:
            destino.depositar(valor)
            return True
