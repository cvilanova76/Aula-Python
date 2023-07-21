from cliente import Cliente
from historico import Historico
import abc
class Conta(abc.ABC):
    _total_de_contas = 1


    def __init__(self, numero, cliente, saldo, limite = 10000.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo= saldo
        self._limite = limite
        self._historico = Historico()

        Conta._total_de_contas += 1

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo
    @property
    def historico(self):
        return self._historico

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo (self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @staticmethod
    def get_identificador():
        return Conta._identificador

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
