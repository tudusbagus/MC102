###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Estudando Cifras
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura de dados

ntrada = "CDFA#MG"

acordes_validos = ['C', 'C#', 'Cm', 'C#m', 'C#M', 'D', 'D#', 'D#m', 'D#M',
                   'E', 'Em', 'F', 'F#', 'F#m', 'F#M', 'G', 'G#', 'G#m', 'G#M',
                   'A', 'A#', 'A#m', 'A#M', 'B', 'Bm']

sequencia_de_notas = []
i = 0

while i < len(entrada):
    # Testar acordes do maior para o menor (ex: "A#M" antes de "A#")
    encontrado = False
    for tamanho in range(3, 0, -1):  # tenta 3 letras, depois 2, depois 1
        candidato = entrada[i:i+tamanho]
        if candidato in acordes_validos:
            sequencia_de_notas.append(candidato)
            i += tamanho
            encontrado = True
            break
    if not encontrado:
        raise ValueError(f"Nota inválida na posição {i}: '{entrada[i:]}'")

# Agora você pode encontrar a posição de "A#M"
if "A#M" in sequencia_de_notas:
    posicao = sequencia_de_notas.index("A#M")
    print("Posição de A#M:", posicao)
else:
    print("A#M não encontrado.")
    