from datetime import datetime

class Historico():
    def __init__(self):
        self._data_abertura = datetime.today()
        self.historico_transacoes = []

    @property
    def data_abertura(self):
        return self._data_abertura

    def exibir_historico(self):
        count = 1;
        print("\nexibindo seu historico")
        for historico in self.historico_transacoes:
            print(f"{count}: {historico}")
            count +=1
