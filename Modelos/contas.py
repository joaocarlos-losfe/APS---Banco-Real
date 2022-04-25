from Modelos.conta import Conta

class Contas():
    def __init__(self):
        self._dict_contas = {}

    def salvar_conta(self,conta):
        if conta.titular.cpf in self._dict_contas.keys():
            return False # não salvou
        else:
            self._dict_contas[conta.titular.cpf] = conta
            return True #salvou 

    #busca por cpf
    def get_conta_cpf(self,cpf) -> Conta:
        if cpf in self._dict_contas.keys():
            return self._dict_contas[cpf]
        else:
            return None

    #busca por numero de conta
    def get_conta_numero(self,numero:str) -> Conta:
        for conta in self._dict_contas.values():
            if conta.numero == numero:
                return conta
        return None