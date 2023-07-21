class Autenticavel:

    def autentica(self, senha):
        if self._senha == senha:
            return True
        else:
            return False

