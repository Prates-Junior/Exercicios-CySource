from socket import *
import threading

servidor = socket(AF_INET,SOCK_STREAM)
servidor.bind(("0.0.0.0",4444))
servidor.listen(5)


# Mensagens dos Clientes
def conexao(clientes):
    while True:
        dados = cliente.recv(2048).decode()
        print(f"Cliente: {dados}")
        # Verifica se o Cliente quer sair
        if dados == "sair":
            cliente.close()
            break


        dados = input('Msg ao Cliente:')
        cliente.sendall(dados.encode())

# Clientes se Conectando

cliente, endereco = servidor.accept()

t = threading.Thread(target=conexao, args=(cliente,))
t.start()
