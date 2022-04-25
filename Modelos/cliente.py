class Cliente():
    def __init__(self, nome:str,sobre_nome:str, cpf:str):
        self._nome = nome
        self._email = sobre_nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def email(self):
        return self._email
