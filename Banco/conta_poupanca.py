from conta import Conta

class ContaPoupanca(Conta):
    pass

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

