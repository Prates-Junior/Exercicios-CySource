import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis

# Inicializa a janela principal
Janela = customtkinter.CTk()
Janela.geometry("400x600")

# Carrega as conversões disponíveis
dic_conversoes_disponiveis = conversoes_disponiveis()

# Define o título e os textos das labels
titulo = customtkinter.CTkLabel(Janela, text="CONVERSOR DE MOEDAS", font=("", 20))
texto_moeda_origem = customtkinter.CTkLabel(Janela, text="Selecione a moeda de origem:")
texto_moeda_destino = customtkinter.CTkLabel(Janela, text="Selecione a moeda de destino:")

# Função para carregar moedas de destino com base na moeda de origem selecionada
def carregar_moedas_destino(moeda_selecionada):
    if moeda_selecionada in dic_conversoes_disponiveis:
        lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
        campo_moeda_destino.configure(values=lista_moedas_destino)
        if lista_moedas_destino:  # Verifica se a lista não está vazia
            campo_moeda_destino.set(lista_moedas_destino[0])  # Define o primeiro valor como selecionado
    else:
        print(f"Moeda {moeda_selecionada} não encontrada em dic_conversoes_disponiveis.")

# Carrega os nomes das moedas disponíveis
moedas_disponiveis = nomes_moedas()

# Define os menus de seleção de moedas
campo_moeda_origem = customtkinter.CTkOptionMenu(
    Janela, values=list(moedas_disponiveis.keys()), command=carregar_moedas_destino
)
campo_moeda_destino = customtkinter.CTkOptionMenu(Janela, values=["Selecione uma moeda de origem"])

# Função de conversão de moeda (atualmente só imprime uma mensagem)
def converter_moeda():
    print("Converter Moeda")

# Botão para realizar a conversão
botao_converter = customtkinter.CTkButton(Janela, text="Converter", command=converter_moeda)

# Adiciona o título à janela
titulo.pack(padx=10, pady=10)

# Frame rolável para listar as moedas disponíveis
lista_moedas = customtkinter.CTkScrollableFrame(Janela)

# Carrega e exibe a lista de moedas disponíveis
for codigo_moedas in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moedas]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moedas}: {nome_moeda}")
    texto_moeda.pack()

# Coloca todos os elementos na tela
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# Inicia a execução da janela
Janela.mainloop()
