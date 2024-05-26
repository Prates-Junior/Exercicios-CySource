import xmltodict




def nomes_moedas():
    with open("moedas.xml","rb") as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    

    moedas = dic_moedas["xml"]
    return moedas

def conversoes_disponiveis():
    with open("conversoes.xml","rb") as arquivo_conversoes:
    
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

        conversoes = dic_conversoes ["xml"]
        dic_conversoes_disponiveis = {}
        for par_coversao in conversoes:
            campo_moeda_origem , campo_moeda_destino = par_coversao.split("-")
            if campo_moeda_origem in dic_conversoes_disponiveis:
                dic_conversoes_disponiveis[campo_moeda_origem].append(campo_moeda_destino)
            else:
                dic_conversoes_disponiveis[campo_moeda_origem] = [campo_moeda_destino]

            return dic_conversoes_disponiveis
