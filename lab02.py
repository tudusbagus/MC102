k = int(input())
P = float(input())
X = float(input())
Y = int(input())
Z = int(input())

N = (((k+Z-1)//Z)*Z)
A = ((k*P)*(1-X/100))
B1 = ((k//Z)*(Y*P)+(k%Z)*P)
B2 = (((N/Z)*(Y*P)))

if (B2<=A):
    print("False")
elif (B1<=A):
    print("False")
else:
    print(True)    
