class Cliente():
    def __init__(self, nome:str,sobre_nome:str, cpf:str):
        self._nome = nome
        self._sobre_nome = sobre_nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def sobre_node(self):
        return self._sobre_nome
