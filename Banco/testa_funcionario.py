from gerente import Gerente
from diretor import Diretor
from cliente import Cliente
from sistem_interno import SistemaInterno

gerente = Gerente('José', '111222333-44', 5000.0, '1234', 0)

diretor = Diretor('Maria', '999000111222-33', 10000.0)

cliente = Cliente("Carolina", "Carvalho", "123456789-00", "1234")

sistema = SistemaInterno()
sistema.login(gerente)
sistema.login(cliente)
sistema.login(diretor)
