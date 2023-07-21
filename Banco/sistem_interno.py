class SistemaInterno:

    def login(self, obj):
        if hasattr(obj, 'autentica'):
            obj.autentica(obj.senha)
            print("Autenticável")
        else:
            print("Não autenticável")