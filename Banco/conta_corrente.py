from conta import Conta

class ContaCorrent(Conta):
    pass

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2