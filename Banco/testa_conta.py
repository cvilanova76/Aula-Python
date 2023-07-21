from conta import Conta
from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from atualizador_conta import AtualizadorConta
from seguro_iphone import SeguroIphone
from manipulador import Manipulador

'''
cliente = Cliente("Carolina", "Carvalho", "123456789-00", "1234")
cp = ContaPoupanca("123-4", cliente, 1000.0)
cc = ContaCorrente("123-4", cliente, 1000.0)

ac = AtualizadorConta(0.1)

ac.roda(cp)
ac.roda(cc)

print("Saldo total: {}".format(ac.saldo_total))
'''

cliente = Cliente("Carolina", "Carvalho", "123456789-00", "1234")
cp = ContaPoupanca("123-4", cliente, 1000.0)
cc = ContaCorrente("123-4", cliente, 1000.0)
seguro = SeguroIphone(1000.0, "Carolina", "1234-5")
lista_tributaveis = []
lista_tributaveis.append(cc)
lista_tributaveis.append(seguro)

manipulador = Manipulador()

total = manipulador.calcula_imposto(lista_tributaveis)

print(total)


