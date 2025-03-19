k = int(input())
P = float(input())
X = float(input())
Y = int(input())
Z = int(input())

A = ((k*P)*(1-X))
B1 = (k*P - ((Z*k*P)/Y))
B2 = (k*P - ((Z*(k+1)*P)/Y))
B = min(((k*P - ((Z*k*P)/Y)) , (k*P - ((Z*(k+1)*P)/Y)))) # Matemática está errada, corrigir
print(A)
print(B)
if (B>A):
    print("True")
else:
    print("False")
