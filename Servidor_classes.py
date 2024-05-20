from socket import *

class servidorSocket(object):
    def __init__(self , endereco, porta):
        self.servidor = socket(AF_INET,SOCK_STREAM)
        self.servidor.bind((endereco,porta))
        self.servidor.listen(100)
        self.fechado = False
    def aceitar(self):
        self.cliente, endereco = self.servidor.accept()

    def __call__(self, *args, **kwargs):
        self.cliente.sendall("Bem Vindo".encode())
        while True:
            #Servidor recebe os dados do cliente
            dados = self.cliente.recv(2048).decode()
            print(f"Cliente {dados}")



            if dados == "sair":
                self.cliente.close()
                self.servidor.close()
                self.fechado = True
                break
                # Servidor envia os  dados de volta ao cliente
            dados = input("[+] Servidor: ")
            self.cliente.sendall(dados.encode())

srv = servidorSocket('',1337)
srv.aceitar()
srv()



