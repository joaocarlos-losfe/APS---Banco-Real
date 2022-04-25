import threading

from datetime import datetime
from Modelos.cliente import Cliente
from Modelos.conta import Conta

from database import Database

class OperacoesServidor:

    def __init__(self):
        self.database = Database()
        self.sinc = threading.Lock()

    def obter_usuario(self, cpf, senha):
        dado = self.database.get_usuario(cpf, senha)

        if dado != False:
            return dado+"/"+self.database.get_cliente(cpf)

        return "False"

    def realizar_cadastro(self, nome, sobre_nome,cpf, senha):

        cliente = Cliente(nome, sobre_nome, cpf)
        conta = Conta(cliente, senha)

        if self.database.adicionar_conta(conta) == "True":
            self.database.set_historico(f"conta aberta dia {conta._historico.data_abertura} Numero: {conta._numero_conta}. Limite: {conta._limite}", cpf)
            return "True/"+conta.numero

        return "False"

    def realizar_saque(self, cpf, valor):

        conta = self.database.get_conta(cpf)

        if type(conta) == tuple:

            if float(valor) > float(conta[2]):
                self.database.set_historico(f"Tentativa de saque dia {datetime.today()} no valor de R$ {float(valor)}", cpf)
                return "False"
            else:
                self.sinc.acquire()
                self.database.atualizar_saldo(cpf, (conta[2] - float(valor)))
                self.sinc.release()
                self.database.set_historico(f"Saque realizado dia {datetime.today()} no valor de R$ {float(valor)}", cpf)
                return "True"

        return "False"


    def realizar_transferencia(self,cpf_origem,conta_destino,valor):

        conta_origem = self.database.get_conta(cpf_origem)
        conta_destino = self.database.get_numero_conta(conta_destino)

        if type(conta_origem) == tuple:

            if float(valor) > conta_origem[2]:
                self.database.set_historico(f"Tentativa de transferencia dia {datetime.today()} no valor de R$ {float(valor)}", cpf_origem)
                return "False"
            elif(conta_destino == None):
                return "False"
            else:
                self.sinc.acquire()
                self.database.atualizar_saldo(cpf_origem,(conta_origem[2] - float(valor)))
                self.sinc.release()
                self.database.set_historico(f"Transferencia realizada dia {datetime.today()} no valor de R$ {float(valor)}", cpf_origem)
                self.sinc.acquire()
                self.database.atualizar_saldo(conta_destino[1], conta_destino[2] + float(valor))
                self.sinc.release()
                self.database.set_historico(f"Transferencia recebida dia {datetime.today()} no valor de R$ {float(valor)} de {cpf_origem}", conta_destino[1])
                return "True"

        return "False"


    def realizar_deposito(self, cpf, valor):
        conta = self.database.get_conta(cpf)
        if type(conta) == tuple:
            self.sinc.acquire()
            self.database.atualizar_saldo(cpf, float(conta[2] + float(valor)))
            self.sinc.release()
            self.database.set_historico(f"Deposito realizado dia {datetime.today()} no valor de R$ {float(valor)}", cpf)
            return "True"

        return "False"


    def carregar_extrato(self, cpf):

        historico = self.database.get_historico(cpf)

        if historico != False:
            return historico

        return "False"


    def operacoes(self, informacoes: str):

        informacoes = informacoes.split('/')

        if informacoes[0] == "cadastro":
            return self.realizar_cadastro(informacoes[1], informacoes[2], informacoes[3], informacoes[4])

        if informacoes[0] == "obter_usuario":
            return self.obter_usuario(informacoes[1], informacoes[2])

        elif informacoes[0] == "saque":
            return self.realizar_saque(informacoes[1], informacoes[2])

        elif informacoes[0] == "transferencia":
            return self.realizar_transferencia(informacoes[1],informacoes[2],informacoes[3])

        elif informacoes[0] == "deposito":
            return self.realizar_deposito(informacoes[1], informacoes[2])

        elif informacoes[0] == "extrato":
            return self.carregar_extrato(informacoes[1])

        else:
            print("informacoes[0] invalida")

        return "False"
