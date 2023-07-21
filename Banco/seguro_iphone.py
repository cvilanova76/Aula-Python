class SeguroIphone:

    def __init__(self, valor, cliente, numero):
        self._valor = valor
        self._cliente = cliente
        self._numero = numero

    def get_valor_imposto(self):
        return 50 + self._valor