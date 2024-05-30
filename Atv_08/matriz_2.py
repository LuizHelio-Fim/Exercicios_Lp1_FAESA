#Adiciona valores aos locais indicados no codigo
A = []
for i in range(5):
    A.append( [0] *5)
A[1][1] = 2
A[3][2] = 4

for lista in A:
    for elemento in lista:
        print(elemento, end=' ')
    print()