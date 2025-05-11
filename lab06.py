###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Roleta da Sorte
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura de dados
n = int(input().strip())  
objetos = []
for _ in range(n):
    linha = input().strip().split(maxsplit=1)
    objetos.append((int(linha[0]), linha[1]))  
k = int(input().strip())  
forcas = list(map(int, input().strip().split())) 

# Processamento dos dados
if k > n:
    print("Não foi possível realizar o sorteio")
    exit()

premios = []
sorteados = set()
posicao = -1  # Começa antes do primeiro

for forca in forcas:
    f = forca
    while True:
        posicao = (posicao + f) % n
        id_atual, nome_atual = objetos[posicao]
        if id_atual not in sorteados:
            premios.append(f"{id_atual}-{nome_atual}")
            sorteados.add(id_atual)
            break
        else:
            if f > 1:
                f -= 1
            else:
                f = 1

# Saída de dados
print(" ".join(premios))               