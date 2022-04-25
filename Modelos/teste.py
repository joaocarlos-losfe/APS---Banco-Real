from conta import Conta
from contas import Contas
from cliente import Cliente

contas = Contas()

if __name__ == '__main__':
    contas = Contas()

    c1 = Cliente('joao', 'de sousa', '111.111.111-11')
    conta1 = Conta(c1, "111")

    print(conta1.numero)
    conta1.exibir_historico()

    c2 = Cliente('joao', 'de sousa', '222.222.222-11')
    conta2 = Conta(c2, "111")

    print(conta2.numero)
    conta2.exibir_historico()

    print(contas.salvar_conta(conta1))
    print(contas.salvar_conta(conta2))


