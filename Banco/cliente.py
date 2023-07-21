from autenticavel import Autenticavel
class Cliente(Autenticavel):
    def __init__(self, nome, sobrenome, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self._senha = senha

    @property
    def senha(self):
        return self._senha



