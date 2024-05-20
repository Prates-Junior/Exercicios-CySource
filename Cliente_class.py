from socket import *

cliente = socket(AF_INET,SOCK_STREAM)
cliente.connect(("127.0.0.1",1337))


while True:
    # Cliente recebe os dados do  Servidor
    dados = cliente.recv(2048).decode()
    print(f"Servidor: {dados}")
       # Cliente envia os dados para o servidor
    dados = input("[+] Cliente: ")
    cliente.sendall(dados.encode())

    # caso o cliente decida encerrar o chat
    if dados == "sair":
        cliente.close()
        break

