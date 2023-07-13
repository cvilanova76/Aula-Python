from conta import Conta
from cliente import Cliente


conta = Conta('123-4', 'Carolina Carvalho', 1000.0, 10000.0)
conta1 = Conta('432-1', 'Pedro Salles', 1000.0, 50000.0)
cliente = Cliente('Carolina', 'Carvalho', '123456789-00')
cliente1 = Cliente('Pedro', 'Salles', '009876543-21')

conta1.depositar(250.0)
conta1.extrato()
conta1.sacar(500.0)
conta1.extrato()
conta1.transferir(conta, 200.0)
conta.extrato()
conta1.extrato()

