import requests

link = 'https://minhaapi.claudiojunior11.repl.co/pegarVendas'
requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['Total_Vendas'])


