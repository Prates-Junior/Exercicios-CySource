from socket import *
import threading

def leitor(clientes):
    while True:
        # Servidor enviando os dados
        dados = cliente.recv(2048).decode()
        print(f'Servidor: {dados}')



cliente = socket(AF_INET,SOCK_STREAM)
cliente.connect(("192.168.0.2",4444))

t = threading.Thread(target=leitor,args=(cliente,))
t.start()

while True:
    # Cliente envia os dados para o servidor
    dados = input('Cliente:')
    cliente.sendall(dados.encode())
    if dados == "sair":
        cliente.close()
        break
    # Servidor recebe os dados do Cliente
    dados = cliente.recv(2048).decode()
    print(f'Servidor {dados}')





