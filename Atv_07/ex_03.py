listaA = [19, 91, 28, 82, 37, 73, 46, 64, 55]
listaB = [61, 85, 99, 95, 73, 61, 59, 11, 61]
listaC = []

for i in range (0, 9):
    if listaA[i] >= listaB[i]:
        listaC.append(listaA[i] - listaB[i])
    else:
        listaC.append(listaB[i] - listaA[i])

print(listaC)