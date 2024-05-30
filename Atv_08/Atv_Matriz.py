from random import uniform

matriz = []
medias = []
position = []
maior = 0

#Gera a Matriz com as notas
for x in range(30):
    linha = []
    for y in range(5):
        n = uniform(0, 10) #gera um float aleatório
        if n > maior:
            position = [(x, y)]
            maior = n
        linha.append(n)
    matriz.append(linha)

#Calcula e salva a media de cada aluno A
for lista in matriz:
    medias.append(sum(lista)/5)


#printa o resultado da lista de notas
print("MATRIZ DE NOTAS DOS ALUNOS:")
for lista in matriz:
    for elemento in lista:
        print("{:.1f}".format(elemento), end='  ')
    print("")

#printa o resultado das medias A
print(" ")
print("MATRIZ DE MÉDIA DOS ALUNOS:")
for lista in medias:
    print("{:.1f}\n".format(lista), end='')
print("")

print("MAIOR NOTA OBTIDA EM CADA COLUNA:")
for lista in position:
    print(f"{position}\n", end='')
print("")