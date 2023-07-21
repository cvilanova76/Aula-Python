from funcionario import Funcionario
from autenticavel import Autenticavel
class Gerente(Funcionario, Autenticavel):

    def __init__(self, nome, cpf, salario, senha, qtd_liderados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_liderados = qtd_liderados

    @property
    def senha(self):
        return self._senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.0


