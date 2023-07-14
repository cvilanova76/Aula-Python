from cliente import Cliente
from historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo= saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de R$ {}".format(valor))

    def sacar(self, valor):
        self.saldo -= valor
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de R$ {}".format(valor))
            return True

    def extrato(self):
        print("numero: {} \ncliente: {} \nsaldo: {}".format(self.numero, self.titular, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de R$ {}".format(self.saldo))

    def transferir(self, destino, valor):
        retirada = self.sacar(valor)
        if retirada == False:
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("transferência de R$ {} para a conta {}".format(valor, destino.numero))
            return True
