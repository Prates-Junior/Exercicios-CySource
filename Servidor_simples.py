from socket import *

servidor = socket(AF_INET,SOCK_STREAM)
servidor.bind(("0.0.0.0",4444))
servidor.listen(5)

# Servidor aceita as conexões
cliente, endereco = servidor.accept()
print(f'Bem Vindo {0}'.format(endereco))


while True:
    # Servidor recebe os dados do Cliente
    dados = cliente.recv(2048).decode()
    print(f'Cliente: {dados}')


    if dados == "sair":
        cliente.close()
        break

    # Servidor envia os dados ao Cliente
    dados = input('Servidor:')
    cliente.sendall(dados.encode())

servidor.close()








