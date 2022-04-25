class Query:

    # MÉTODOS DE CRIAÇÃO DAS TABELAS

    @staticmethod
    def create_table_client():
        return """
                CREATE TABLE IF NOT EXISTS Clientes
                (
                    CPF VARCHAR(14) NOT NULL PRIMARY KEY,
                    Nome VARCHAR(20) NOT NULL,
                    Sobrenome VARCHAR(50) NOT NULL
                );
                """

    @staticmethod
    def create_table_conta():
        return """
            CREATE TABLE IF NOT EXISTS Contas
            (
                numero VARCHAR(15) NOT NULL PRIMARY KEY,
                cpf_titular VARCHAR(8) NOT NULL,
                saldo FLOAT NOT NULL,
                senha TEXT NOT NULL,
                limite FLOAT NOT NULL,
                FOREIGN KEY (cpf_titular) REFERENCES Clientes(CPF)
            );
        """
    @staticmethod
    def create_table_historico():
        return """
            CREATE TABLE IF NOT EXISTS Historicos
            (
                ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                historico TEXT NOT NULL,
                cpf_titular VARCHAR(15) NOT NULL,
                FOREIGN KEY (cpf_titular) REFERENCES Clientes(CPF)
            );
        """

    # MÉTODOS DE SALVAMENTO DE DADOS

    @staticmethod
    def query_save_cliente():
        return  """
                INSERT INTO Clientes(CPF,Nome,Sobrenome)
                VALUES (%s,%s,%s)
                """
    @staticmethod
    def query_save_date_conta():
        return  """
                INSERT INTO Contas(numero, cpf_titular, saldo, senha, limite)
                VALUES (%s,%s,%s,MD5(%s),%s)
                """
    @staticmethod
    def query_save_date_historico():
        return  """
                INSERT INTO Historicos(historico, cpf_titular) VALUES (%s,%s);
                """

    # MÉTODOS DE ATUALIZAÇÃO DE DADOS

    @staticmethod
    def query_update_cliente():
        return  """
                UPDATE Cliente
                SET Nome = %s,Sobrenome = %s,Senha = %s
                WHERE CPF = %s;
                """

    @staticmethod
    def query_atualizar_saldo():
        return  """
                UPDATE Contas SET saldo = %s where cpf_titular = %s;
                """

    def query_get_usuario():
        return  """
                SELECT cpf_titular FROM Contas where cpf_titular = %s AND senha = MD5(%s);
                """

    @staticmethod
    def query_get_cliente():
        return  """
                    SELECT Nome, Sobrenome FROM Clientes WHERE CPF = %s;
                """

    @staticmethod
    def query_update_conta():
        return  """
                UPDATE Contas
                SET cpf_titular = %s, saldo = %s, senha = %s, limite = %s
                WHERE numero = %s;
                """
    @staticmethod
    def query_update_historico():
        return  """
                UPDATE Historico
                SET historico = %s
                WHERE numero_conta = %s;
                """


    @staticmethod
    def query_get_conta():
        return  """
                    SELECT * FROM Contas WHERE cpf_titular = %s;
                """
    @staticmethod
    def query_get_numero_conta():
        return  """
                    SELECT * FROM Contas WHERE numero = %s;
                """
    @staticmethod
    def query_get_historico():
        return  """
                    SELECT historico FROM Historicos WHERE cpf_titular = %s;
                """
    # FIM