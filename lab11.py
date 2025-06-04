###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Organizando a Agenda da Semana
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura da agenda inicial
agenda = [input().split() for _ in range(5)]

def print_agenda(agenda):
    print(' '.join([j.ljust(10) for j in ['Horário', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']]))
    horario = list(range(8, 19))
    for i in range(10):
        saida = [(str(horario[i]) + '-' + str(horario[i+1])).ljust(10)]
        saida += [agenda[j][i].ljust(10) for j in range(5)]
        print(' '.join(saida))

# Mapeia dia para índice
dias = {
    "Segunda": 0,
    "Terça": 1,
    "Quarta": 2,
    "Quinta": 3,
    "Sexta": 4
}

def remover(dia, inicio, fim):
    d = dias[dia]
    começou = inicio - 8
    acabou = fim - 8
    for i in range(começou, acabou):
        agenda[d][i] = "Livre"

def adicionar(nome, duracao):
    for d in range(5):
        horarios = agenda[d]
        for i in range(11 - duracao):
            if all(horarios[i + j] == "Livre" for j in range(duracao)):
                # Aloca a atividade
                for j in range(duracao):
                    horarios[i + j] = nome
                return True

n = int(input())

for _ in range(n):
    comando = input().split()
    if comando[0] == "Remover":
        # Remover D I F
        _, dia, inicio, fim = comando
        remover(dia, int(inicio), int(fim))
    else:
         # Adicionar T H
        _, nome, duracao = comando
        duracao = int(duracao)
        if not adicionar(nome, duracao):
            print(f"Não foi possível alocar a atividade {nome}")



# Imprime agenda atualizada
print_agenda(agenda)
