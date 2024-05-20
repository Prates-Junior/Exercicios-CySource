import os

def get_ip():
        ip = os.popen("ipconfig")
        for linha in ip.readlines():
            if "IPv4" in linha:
                inicio = linha.find(":")
                saida = (linha[inicio+2:-1])
                break
        return saida



def scanner(endereço_ip,clientes,lock):
    resultado = os.popen("ping {0} -n 1".format(endereço_ip,)).read()
    if "TTL" in resultado:
        with lock:
            clientes.append(endereço_ip)
            print(endereço_ip)



if __name__ == "__main__":
    print(get_ip())
    print("aaaaaa")