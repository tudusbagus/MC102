###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Filtro de Carros
# Nome: João Pedro Masson Barnabé
# RA: 281638
###################################################

# Leitura das especificações do cliente
K = int(input())  # Número mínimo de características aceitas pelo cliente
tem_ar = input()  # Possui ar condicionado
tem_dir_hid = input()  # Possui direção hidráulica
quant_cil_li, quant_cil_ls = map(int, input().split())  # Quantidade de cilindradas
tem_vid_el = input()  # Possui vidros elétricos
cap_mal_li, cap_mal_ls = map(int, input().split())  # Capacidade do porta-malas
tem_camb_auto = input()  # Possui câmbio automático
quant_cav_li, quant_cav_ls = map(int, input().split())  # Quantidade de cavalos de potência
quant_gar_li, quant_gar_ls = map(int, input().split())  # Quantidade de meses de garantia
tem_abs = input()  # Possui freios ABS
quant_lug_li, quant_lug_ls = map(int, input().split())  # Quantidade de lugares

# Leitura dos modelos de carros disponíveis
N = int(input())  # Número de modelos disponíveis
modelos_selecionados = []

for _ in range(N):
    modelo_nome = input()  # Nome do modelo
    carro = []
    
    # Características do carro
    carro.append(input())  # Possui ar condicionado
    carro.append(input())  # Possui direção hidráulica
    carro.append(int(input()))  # Quantidade de cilindradas
    carro.append(input())  # Possui vidros elétricos
    carro.append(int(input()))  # Capacidade do porta-malas
    carro.append(input())  # Possui câmbio automático
    carro.append(int(input()))  # Quantidade de cavalos de potência
    carro.append(int(input()))  # Quantidade de meses de garantia
    carro.append(input())  # Possui freios ABS
    carro.append(int(input()))  # Quantidade de lugares
    
    atendidas = 0  # Contador de características atendidas pelo modelo
    
    # Verificando as características de acordo com as especificações do cliente
    if tem_ar == 'P' and carro[0] == 'P' or tem_ar == 'A' and carro[0] == 'A' or tem_ar == 'I':
        atendidas += 1
    if tem_dir_hid == 'P' and carro[1] == 'P' or tem_dir_hid == 'A' and carro[1] == 'A' or tem_dir_hid == 'I':
        atendidas += 1
    if quant_cil_li <= carro[2] <= quant_cil_ls:
        atendidas += 1
    if tem_vid_el == 'P' and carro[3] == 'P' or tem_vid_el == 'A' and carro[3] == 'A' or tem_vid_el == 'I':
        atendidas += 1
    if cap_mal_li <= carro[4] <= cap_mal_ls:
        atendidas += 1
    if tem_camb_auto == 'P' and carro[5] == 'P' or tem_camb_auto == 'A' and carro[5] == 'A' or tem_camb_auto == 'I':
        atendidas += 1
    if quant_cav_li <= carro[6] <= quant_cav_ls:
        atendidas += 1
    if quant_gar_li <= carro[7] <= quant_gar_ls:
        atendidas += 1
    if tem_abs == 'P' and carro[8] == 'P' or tem_abs == 'A' and carro[8] == 'A' or tem_abs == 'I':
        atendidas += 1
    if quant_lug_li <= carro[9] <= quant_lug_ls:
        atendidas += 1

    # Se o modelo atende ao número mínimo de características exigidas, adicionamos ao resultado
    if atendidas >= K:
        modelos_selecionados.append(modelo_nome)

# Exibindo os modelos selecionados
print("Modelos selecionados:")
for modelo in modelos_selecionados:
    print(modelo)