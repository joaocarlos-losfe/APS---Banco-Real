class Estilos():

    def estilo_botao_navegacao(self):
        return """
                QPushButton
                {
                    color: white; 
                    font-size: 14px;
                    font-weight: bold; 
                    margin-top: 8px; 		
                    margin-bottom: 8px; 
                    padding: 10px;
                    text-align: left;
                    border-radius: 10px;
                }

                QPushButton:hover
                {
                    transition: all 1s ease-out;
                    background-color: #646464;
                }
                
                QPushButton:pressed
                {
                    background-color: #434343;
                }
               """

    def estilo_botao_navegacao_clicado(self):
        return """
                QPushButton
                {
                    color: white; 
                    font-size: 14px;
                    font-weight: bold; 
                    margin-top: 8px; 		
                    margin-bottom: 8px; 
                    padding: 10px;
                    text-align: left;
                    border-radius: 10px;
                    background-color: #646464;
                }

                QPushButton:hover
                {
                    transition: all 1s ease-out;
                    background-color: #646464;
                }

                QPushButton:pressed
                {
                    background-color: #434343;
                }
               """
    def estilo_entradas(self):
        return  """
                QLineEdit
                {
                    background-color: #6C6C6C; 
                    color: white; 
                    padding: 5px; 
                    corner-radius: 10px; 
                    font-size: 12px; 
                    font-weight: bold; 
                    border-radius: 5px;
                }
                """

    def estilo_botoes_confirmacao(self):
        return  """
                QPushButton
                {
                    background-color: #333333; 
                    color: white; 
                    padding: 8px; 
                    font-weight: bold; 
                    font-size: 12px; 
                    border-radius: 8px;
                }
                
                QPushButton:hover
                {
                    transition: all 1s ease-out;
                    background-color: #646464;
                }

                QPushButton:pressed
                {
                    background-color: #434343;
                }
                """

    def estilo_entradas(self):
        return """
                QLineEdit
                {
                    background-color: #6C6C6C; 
                    color: white; 
                    padding: 5px; 
                    corner-radius: 10px; 
                    font-size: 12px; 
                    font-weight: bold; 
                    border-radius: 5px;
                }
                """

    def estilo_botoes_cancelamento(self):
        return """
                QPushButton
                {
                    background-color: #505050; 
                    color: white; 
                    padding: 8px; 
                    font-weight: bold; 
                    font-size: 12px; 
                    border-radius: 8px;
                }

                QPushButton:hover
                {
                    transition: all 1s ease-out;
                    background-color: #646464;
                }

                QPushButton:pressed
                {
                    background-color: #434343;
                }
                """