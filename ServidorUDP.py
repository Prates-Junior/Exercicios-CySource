from socket import *


servidor = socket(AF_INET, SOCK_DGRAM)
servidor.bind(("", 3333))


while True:
    print ("Esperando conexão")
    dados, cliente = servidor.recvfrom(2048)
    print (dados.decode())

    if dados.decode() == "sair":
        servidor.close()
        break

    dados = input("Servidor: ")
    servidor.sendto(dados.encode(), cliente)