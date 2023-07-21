from conta import Conta
from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from atualizador_conta import AtualizadorConta


cliente = Cliente("Carolina", "Carvalho", "123456789-00")
cp = ContaPoupanca("123-4", cliente, 1000.0)
cc = ContaCorrente("123-4", cliente, 1000.0)

ac = AtualizadorConta(0.1)

ac.roda(cp)
ac.roda(cc)

print("Saldo total: {}".format(ac.saldo_total))

