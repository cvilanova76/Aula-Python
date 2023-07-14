import datetime


class Historico:

    def __init__(self):
        self.data_abertura = datetime.date.today()
        self.transacoes = []

    def imprimir(self):
        print("Data de abertura: {}".format(self.data_abertura))
        print("transacoes: ")
        for t in self.transacoes:
            print('-', t)



