X = float(input()) # Orçamento disponível
Y = (input()) # Clima: E (ensolarado); N (nublado); C (chuvoso)
Z = (input()) # Tempo livre: P (pouco); M (médio); A (alto)

if (X<=500 and Y == "C"):
    print("Descansar")
elif (X<=500 and Z == "M"):
        print("Caminhada")
elif (X<=500 and Z == "A"):
    print("Piscina")
elif (X<=500 and Z == "P"):
     print("Descansar") 

elif(X>500 and Z == "P"):
    print("Descansar")
elif (X>500 and Y == "C" and Z != "P"):
    print("Leitura")
elif (X>500 and Y != "C" and Z == "A"):
    print("Praia")
elif (X>500 and Y == "E" and Z == "M"):
    print("Caminhada")
else:
    print("Cinema")
