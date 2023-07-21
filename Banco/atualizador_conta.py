class AtualizadorConta:

    def __init__(self, taxa, saldo_total = 0):
        self._taxa = taxa
        self._saldo_total = saldo_total

    def roda(self, conta):
        print("Saldo inicial da conta: {}".format(conta.saldo))
        atualiza = conta.atualiza(self._taxa)
        self._saldo_total += atualiza
        print("Saldo final: {}".format(atualiza))

    @property
    def saldo_total(self):
        return self._saldo_total

