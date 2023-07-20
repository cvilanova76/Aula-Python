from gerente import Gerente
#from funcionario import Funcionario
from controle_bonificacao import ControleBonificacao
from diretor import Diretor

gerente = Gerente('José', '111222333-44', 5000.0, '1234', 0)
print('bonificação gerente: {}'.format(gerente.get_bonificacao()))

#funcionario = Funcionario('João', '444555666-77', 2000.0)
#print('bonificação funcionario: {}'.format(funcionario.get_bonificacao()))

diretor = Diretor('Maria', '999000111222-33', 10000.0)
print('bonificação diretor: {}'.format(diretor.get_bonificacao()))

controle = ControleBonificacao()
#controle.registro(funcionario)
controle.registro(gerente)
print("total: {}".format(controle._total_bonificacao))





