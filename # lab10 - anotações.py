# lab10 - anotações sobre matrizes

i = int(input()) # linhas
j = int(input()) # colunas
matriz = []

for (i) in range:
    linha = [] # número de linahs
    for j in range:
        linha.append(int(input())) # números da matriz
matriz.append(linha)        

# No exemplo estamos percorrendo primeiro o número de linhas (de acordo com a variável i), depois, inserimos os dados
#da matriz (neste caso, inteiros) como um elemento de cada linha, assim dfinindo o número de colunas (dado por j)

print(matriz)

# Isso também serve se quisermos escrever uma atriz pré definida, exemplos, uma matirz só com 0s, mas na linha 10
#não usariamos int(input()), mas sim (0)

# Forma alternativa/compacta de inicializar uma matriz

matriz = [[0 for j in range(c)] for i in range(l)]

#---------------------------------------------------------------------

# Para acessarmos elementos de uma matriz, usamos matriz[linha][coluna], com linhas e colunas indo de 0 a n
# Podemos também alterar um elemento da matriz da seguinte forma matriz[linha][coluna] = valor
# Exemplos

matriz = [[1,2,3],[4,5,6][7,8,9]]
print(matriz[2][1])

matriz = [[1,2,3],[4,5,6][7,8,9]]
matriz[[2][1]] = 10
print(matriz[2][1])

#---------------------------------------------------------------------

# Podemos também copiar uma matriz, mas para isso a nova matriz devera ser vazia (e de mesma tamanho)

A = [[1,2,3],[4,5,6],[7,8,9]]
B = A.copy()
B = [[0],[0],[0]]

print(B)

# Podendo ser feito como

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [linha.copy() for linha in A] # Modo mais elegante: B = [linha[:] for linha in A] ou: B = [list(linha) for linha in A]
B = [[0],[0],[0]]

print(B)

# Exercícios

# 1. Escreva uma função que leia e retorne uma matriz de inteiros
#fornecida pelo usuário. Sua função deve ler os números linha a linha.
#Os números devem estar separados por espaços em branco. Sua
#função deve interromper a leitura ao receber uma linha em branco.

i = int(input()) # linhas
j = int(input()) # colunas
matriz = []

for (i) in range:
    linha = [] # número de linahs
    for j in range:
        linha.append(int(input())) # números da matriz
matriz.append(linha)
