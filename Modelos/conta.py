import random

from Modelos.cliente import Cliente
from Modelos.historico import Historico
from random import randint
from datetime import datetime

class Conta():

    _contador_contas = 0

    __slots__ = ['_numero_conta', '_titular', '_senha_acesso', '_saldo', '_limite', '_historico']

    # titular é do tipo Cliente()

    def __init__(self, titular:Cliente, senha_acesso:str, limite = 10000):
        self._numero_conta = f"{randint(1000, 9999)}" + f" {randint(1000, 9999)}" + f" {randint(1000, 9999)}"
        self._titular = titular
        self._senha_acesso = senha_acesso
        self._saldo = 0.0
        self._limite = limite
        self._historico = Historico()
        Conta._contador_contas += 1
     
        self._definir_historico(f"conta aberta dia {self._historico.data_abertura}. Numero: {self._numero_conta}. Limite: {self._limite}")

    @property
    def saldo(self):
        return self._saldo

    @property
    def senha(self):
        return self._senha_acesso

    @property
    def numero(self):
        return self._numero_conta

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite


    def exibir_historico(self):
        self._historico.exibir_historico()

    def _definir_historico(self, msg):
        self._historico.historico_transacoes.append(msg)

    def depositar(self, valor:float):
        self._saldo += valor
        self._definir_historico(f"deposito no valor de R$ {valor} dia {datetime.today()}. saldo na data do deposito: R$ {self._saldo}")

    def sacar(self, valor:float):
        if(valor > self._saldo or valor <= 0):
            self._definir_historico(f"tentativa de saque no valor de R$ {valor} dia {datetime.today()}")
            return False
        else:
            self._saldo -= valor
            self._definir_historico(f"saque realizado no valor de R$ {valor} dia {datetime.today()}. saldo na data do saque: R$ {self._saldo}")
            return True

    def transfere(self, conta_destino, valor):
        if(self._saldo < valor):
            self._definir_historico(f"tentativa de transferencia para a conta {conta_destino._numero_conta}. saldo insuficiente para transaferencia")
            return False
        else:
            self.sacar(valor)
            self._definir_historico(f"transferencia realizada para a conta {conta_destino._numero_conta}")
            conta_destino._definir_historico(f"você recebeu uma transferencia de {self._titular.nome}. no valor de {valor}")
            conta_destino.depositar(valor)
            return True

    def get_historico(self):
        return self._historico.get_historico()

    @staticmethod
    def quantidade_contas():
        return Conta._contador_contas
