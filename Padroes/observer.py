from Modelos.sendEmail import SendEmail

from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class notify_new_account(Observer):

    def __init__(self, observer):
        self._observer = observer
        observer.attach(self)
        
    def update(self):
        Enviar = SendEmail()
        Enviar.sendEmail(self._observer.titular.email, 'Banco Real: Abertura de conta',f'{self._observer.titular.nome}, Bem-vindo ao Banco Real!\nSua conta é: {self._observer.numero}')

#transferencia
class notify_new_transfer(Observer):
    def __init__(self, observer):
        self._observer = observer
        observer.attach(self)
    
    def update(self):
        mail = SendEmail()
        mail.sendEmail(self._observer.titular.email,'Banco Real: transfência realizada com sucesso', f'Operação Transferencia realizada com sucesso!')

#deposito
class notify_new_deposit(Observer):
    def __init__(self, observer):
        self._observer = observer
        observer.attach(self)
    
    def update(self):
        mail = SendEmail()
        mail.sendEmail(self._observer.titular.email,'Banco Real: depósito realizado com sucesso' ,f'Operação depósito realizado com sucesso!')

#sacar
class notify_new_withdraw(Observer):
    def __init__(self, observer):
        self._observer = observer
        observer.attach(self)
    
    def update(self):
        mail = SendEmail()
        mail.sendEmail(self._observer.titular.email,'Banco Real: saque realizado com sucesso', f'Operação saque realizado com sucesso!')