###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Corredor RPG
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura do corredor

n = input()
corredor = list(n)
print(corredor)
if "1" or "2" or "3" in corredor:
    print(corredor.index("1"))

# Leitura dos valores dos dados e simulação do jogo

posiçoes_monstro1 = [i for i, casa in enumerate(corredor) if casa == "1"]
posiçoes_monstro2 = [i for i, casa in enumerate(corredor) if casa == "2"]
posições_monstro3 = [i for i, casa in enumerate(corredor) if casa == "3"]

posição_inicial = corredor(0)
posição = corredor(0)
vidas_iniciais = 3

andar = int(input())
atacar = int(input())

while posição <= len(corredor):
    dado_de_posição = int(input()) #lançamento do dado de posição
    posição =+ dado_de_posição
    if (posição == (posiçoes_monstro1)):
        dado_de_ataque = int(input())
        if dado_de_ataque >= 3:

        



# Impressão da saída