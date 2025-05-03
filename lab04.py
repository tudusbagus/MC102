###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Batalha na Ponte de Piltover I
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura dos parametros da batalha

Vj = int(input())
Ve = int(input())
Dj = int(input())
De = int(input())
Rj = int(input())
Re = int(input())
Cj = int(input())
Ce = int(input())

Vj_inicial = Vj 
Ve_inicial = Ve

# Leitura da sequência de ataques e determinação do vencedor

turno = input("Quem começa? (J para Jinx, E para Ekko): ")
ultimo_turno = turno
i = 1

while (Vj > 0 and Ve > 0):
    print("Novo turno")
    if turno == "J":
        Ve = Ve - Dj
        Vj = Vj + (Rj * Vj_inicial / 100)
        if Vj > Vj_inicial:
           Vj = Vj_inicial
        print("Vida de Jinx após regeneração: {}".format(Vj))
        print("Vida de Ekko após dano: {}".format(Ve))
        if turno == ultimo_turno:
            i += 1
        else:
            i = 1
        if i == Cj:
            Dj *= 2
            print("Dano de Jinx após aumento: {}".format(Dj))
        
        ultimo_turno = "J"
        turno = input("Digite o próximo turno (J para Jinx, E para Ekko): ")
    
    else:
        Vj = Vj - De
        Ve = Ve + (Re * Ve_inicial / 100)
        if Ve > Ve_inicial:
           Ve = Ve_inicial
        print("Vida de Ekko após regeneração: {}".format(Ve))
        print("Vida de Jinx após dano: {}".format(Vj))
        if turno == ultimo_turno:
            i += 1
        else:
            i = 1
        if i == Ce:
            De *= 2
            print("Dano de Ekko após aumento: {}".format(De))
        
        ultimo_turno = "E"
        turno = input("Digite o próximo turno (J para Jinx, E para Ekko): ")

if Ve <= 0 and Vj > 0:
    print("Jinx vence")
elif Vj <= 0 and Ve > 0:
    print("Ekko vence")