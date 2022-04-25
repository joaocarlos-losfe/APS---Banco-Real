import threading
from operacoes import OperacoesServidor
import socket

class ServerThread(threading.Thread):
    def __init__(self, informacoes_cliente:str, socket, addr):
        threading.Thread.__init__(self)
        self.socket = socket
        self.addr = addr
        self.operacoes = OperacoesServidor()
        self.inf = informacoes_cliente

    def run(self):
        print(f"cliente id {self.addr}")
        mensagem_servidor = self.operacoes.operacoes(self.inf)
        self.socket.send(mensagem_servidor.encode())
        self.socket.close()

if __name__=='__main__':

    host = "localhost"
    porta = 8000
    endereco = (host, porta)
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor_socket.bind(endereco)
    servidor_socket.listen(1)

    print("servidor iniciado")

    while True:
        
        clientsock, clientAddr = servidor_socket.accept()
        mensagem_cliente = clientsock.recv(1024)
        mensagem_cliente = mensagem_cliente.decode()

        if mensagem_cliente != "~desconetar~":
            cliente_thread = ServerThread(mensagem_cliente, clientsock, clientAddr)
            cliente_thread.start()
        else:
            break; 
             
    servidor_socket.close()


        
