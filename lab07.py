###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Corredor RPG
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura do corredor

n = input()
corredor = list(n)

# Leitura dos valores dos dados e simulação do jogo
posicoes_monstro1 = [i for i, casa in enumerate(corredor) if casa == "1"]
posicoes_monstro2 = [i for i, casa in enumerate(corredor) if casa == "2"]
posicoes_monstro3 = [i for i, casa in enumerate(corredor) if casa == "3"]

posicao = 0
vidas = 3

while posicao < len(corredor):
    dado_de_posicao = int(input())
    posicao += dado_de_posicao

    if posicao >= len(corredor):
        break

    if posicao in posicoes_monstro1:
        dado_de_ataque = int(input())
        if dado_de_ataque >= 3:
            corredor[posicao] = "."
            posicoes_monstro1.remove(posicao)
            continue
        else:
            vidas -= 1
            posicao = 0
    elif posicao in posicoes_monstro2:
        dado_de_ataque = int(input())
        if dado_de_ataque >= 5:
            corredor[posicao] = "."
            posicoes_monstro2.remove(posicao)
            continue
        else:
            vidas -= 1
            posicao = 0
    elif posicao in posicoes_monstro3:
        dado_de_ataque = int(input())
        if dado_de_ataque == 6:
            corredor[posicao] = "."
            posicoes_monstro3.remove(posicao)
            continue
        else:
            vidas -= 1
            posicao = 0

    if vidas <= 0:
        break

# Impressão da saída
if vidas <= 0:
    print("O jogador perdeu.")
else:
    print("O jogador chegou ao fim!")