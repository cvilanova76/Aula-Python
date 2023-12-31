from conta import Conta
from tributavelmixin import TributavelMixin

class ContaCorrente(Conta, TributavelMixin):
    pass

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def get_valor_imposto(self):
        return self._saldo * 0.01


