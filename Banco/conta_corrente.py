from conta import Conta

class ContaCorrente(Conta):
    pass

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

