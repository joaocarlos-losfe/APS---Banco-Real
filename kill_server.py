import socket

try:
    print("---killing server...---")

    host = "localhost"
    porta = 8000
    endereco = (host, porta)

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(endereco)

    mensagem_cliente = ''
    mensagem_servidor = ''

    mensagem_cliente = "~desconectar~"
    cliente_socket.send(mensagem_cliente.encode())

    mensagem_servidor = cliente_socket.recv(1024)
    mensagem_servidor = mensagem_servidor.decode()
    print(f"server response: {mensagem_servidor}")

    cliente_socket.close()
    print("dados enviados")
    print("conexao encerrada...")
                
except:
    print("servidor nao esta em execucao...")


