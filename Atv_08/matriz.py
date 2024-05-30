#Como funciona matrizes - basico -
matriz = []

tamanho_x = int(input("Forneça a quantidade de linhas da matriz: "))
tamanho_y = int(input("Forneça a quantidade de colunas da matriz: "))
for x in range(tamanho_x):
    lista = []
    for y in range(tamanho_y):
        lista.append(0)
    matriz.append(lista)

#Maneira de printar uma matriz com as linhas e as colunas certas
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()