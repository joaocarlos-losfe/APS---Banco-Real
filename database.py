import os
from logging import Logger
from typing import List, Tuple
import mysql.connector as mysql
from querys import Query
from Modelos.conta import Conta

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SendEmail():
    def __init__(self) -> None:

        # create message object instance
        self._msg = MIMEMultipart()
        # setup the parameters of the message
        self._password = "tjzbdmfudgvaxucd"
        self._msg['From'] = "hjunior854@gmail.com"

        # create server
        self._server = smtplib.SMTP('smtp.gmail.com: 587')

        self._server.starttls()

        # Login Credentials for sending the mail
        self._server.login(self._msg['From'], self._password)

    def sendEmail(self, toEmail="wendelnunes9999@gmail.com", descricao="Subscription", message="Corpo da mensssagem da vazia!"):
        # message = message
        # add in the message body
        self._msg.attach(MIMEText(message, 'plain'))

        self._msg['To'] = toEmail
        self._msg['Subject'] = descricao

        # send the message via the server.
        self._server.sendmail(self._msg['From'],
                              self._msg['To'], self._msg.as_string())

        self._server.quit()

class Database:

    def __init__(self):

        self.conexao = mysql.connect(host = 'sql368.main-hosting.eu', db = 'u831868453_aps_areal_bank', user = 'u831868453_user_aps_areal', passwd = 'L0@xF*f+')
        self.cursor = self.conexao.cursor()
        self.inicializar_db()


    def inicializar_db(self):
        self.cursor.execute(Query.create_table_client())
        self.cursor.execute(Query.create_table_conta())
        self.cursor.execute(Query.create_table_historico())

    def adicionar_conta(self, conta:Conta):

        try:
            self.cursor.execute(Query.query_save_cliente(), (conta.titular.cpf, conta.titular.nome, conta.titular.email))
            self.cursor.execute(Query.query_save_date_conta(), (conta.numero, conta.titular.cpf, conta.saldo, conta.senha, conta.limite))
            self.conexao.commit()
            
            Enviar = SendEmail()
            Enviar.sendEmail(conta.titular.email,'Banco Real: Abertura de conta',f'{conta.titular.nome}, Bem-vindo ao Banco Real!\nSua conta é: {conta._numero_conta}')

            return "True"

        except BaseException as e:
            Logger.error('Failed to do something: ' + str(e))
            return "False"

    def get_conta(self, cpf:str):
        self.cursor.execute(Query.query_get_conta(), (cpf, ))
        return self.cursor.fetchone()

    def get_numero_conta(self,numero:str):
        self.cursor.execute(Query.query_get_numero_conta(),(numero,))
        return self.cursor.fetchone()

    def atualizar_saldo(self, cpf:str, valor:float):
        self.cursor.execute(Query.query_atualizar_saldo(), (valor, cpf,))
        self.conexao.commit()

    def get_usuario(self, cpf, senha):
        self.cursor.execute(Query.query_get_usuario(), (cpf, senha,))
        dados = self.cursor.fetchone()
        if type(dados) == tuple:
            self.conexao.commit()
            return str(dados[0])

        else:
            return False

    def get_cliente(self, cpf:str):
        self.cursor.execute(Query.query_get_cliente(), (cpf,))
        dados = self.cursor.fetchone()
        if type(dados) == tuple:
            return dados[0]+"/"+dados[1]
        return False

    def set_historico(self, text:str, cpf:str):
        self.cursor.execute(Query.query_save_date_historico(), (text,cpf,))
        self.conexao.commit()

    def get_historico(self, cpf):

        historico = ""

        self.cursor.execute(Query.query_get_historico(), (cpf,))
        dados = self.cursor.fetchall()

        if len(dados)> 0:
            for dado in dados:
                historico += dado[0] + "/"

            return historico

        return False

#db = Database()

#print(db.get_numero_conta('2430 6079 3607'))
#print(db.get_numero_conta('2430 6079 3606'))
#db.get_usuario(777, "arrozcomfeijao")

#print(db.get_cliente("111"))

#db.get_historico("111")
