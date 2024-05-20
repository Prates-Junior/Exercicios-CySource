from socket import *
import threading

servidor = socket(AF_INET,SOCK_STREAM)
servidor.bind(("0.0.0.0",4444))
servidor.listen(5)

clientes = []

# Mensagens dos Clientes
def conexao(clientes):
    while True:
        dados = cliente.recv(2048).decode()
        print(f"Cliente: {dados}")
        # Verifica se o Cliente quer sair
        if dados == "sair":
            clientes.remove(cliente) # remove cliente específico
            cliente.close()
            break
            # Todos o clientes recebem o envio do Servidor
        for msg in clientes:
            msg.sendall(dados.encode())

# Clientes se Conectando
cliente, endereco = servidor.accept()
clientes.append(cliente)

t = threading.Thread(target=conexao, args=(clientes,))
t.start()
