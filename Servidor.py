from socket import *

servidor = socket(AF_INET, SOCK_STREAM) #Familia de endereços Ipv4 (AF_INET, SOCK_STREAM) TCP,ou UDP (socket(AF_INET, SOCK_DGRAM)
servidor.bind(("0.0.0.0", 1234)) # Método Bind! A configuração de socket , (método usado para conectar o endereço(endereço IP, número da porta) ao socket.)
servidor.listen(5) # quantas estações (Clientes/pessoas/Usuários) podem se conectar ao socket

# Servidor aceita as conexoes
cliente,endereco = servidor.accept()
print(f'Bem Vindo {endereco} ') # Imprime endereço ip do Cliente


# colocar a conexão em um loop while

while True:
    #recebendo dados de forma binaria
        dados= cliente.recv(2048).decode() # Decodificando pacote binário dos Dados
        print(f'Recebido do Cliente: {dados}')
        if dados == "sair": # Se o cliente decidir encerrar a conversa
            cliente.close()
            break

        cliente.sendall('Obrigado'.encode()) # Servidor envia resposta de volta

# fechar servidor
servidor.close()









