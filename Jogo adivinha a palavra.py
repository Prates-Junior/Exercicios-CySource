import eel
import random

palavras = []
situaçao_jogo = []
tentativas = 0

@eel.expose
def iniciar_jogo():
    global palavra # palavra-chave para usar variáveis dentro de função (Global)
    palavra = list(random.choice(['ItSafe','python','cyber','hacking','verde']))
    for item in range(len(palavra)):
        situaçao_jogo.append("_")
    return "|".join(situaçao_jogo)

@eel.expose
def adivinhar_letra(letra):
    global tentativas # palavra-chave para usar variáveis dentro de função (Global)
    tentativas += 1

    if palavra.count(letra): # Verifica se a letra existe, dentro das palavras que foram sorteadas
        for index, data in enumerate(palavra):
            if letra == data: # se os dados que o usuário colocou, baterem
                situaçao_jogo[index] = letra # retorna a letra na posição correspondente
    if situaçao_jogo.count("_") == 0: # Verifica se o jogo foi encerrado, se sim?
        return ("Você acertou em {0} tentativas. A palavra era '{1}',".format(tentativas," ".join(palavra)))


    return "_".join(situaçao_jogo)





eel.init('web')
eel.start('index.html', mode = 'Brave', size=(850,400), port=0)   #python will select free ephemeral ports.


