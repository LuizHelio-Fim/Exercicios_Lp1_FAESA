from random import uniform

matriz = []
medias = []
maiores_valores = []

#Gera a Matriz com as notas
for x in range(30):
    linha = []
    for y in range(5):
        n = uniform(0, 10) #gera um float aleatório
        linha.append(n)

    matriz.append(linha)

#Calcula e salva a media de cada aluno A
for lista in matriz:
    medias.append(sum(lista)/5)

# Calcula o maior valor de cada coluna B
maiores_valores = [max(coluna) for coluna in zip(*matriz)]

#Calcula a media geral da turma C
media_geral = sum(medias)/len(medias)

#printa o resultado da lista de notas
print("MATRIZ DE NOTAS DOS ALUNOS:")
for lista in matriz:
    for elemento in lista:
        print("{:.1f}".format(elemento), end='  ')
    print("")

#printa o resultado das medias A
print(" ")
print("MÉDIA DOS ALUNOS:")
for lista in medias:
    print("{:.1f}\n".format(lista), end='')
print("")

#printa o resultado da maior nota em cada coluna B
print(" ")
print("MAIOR NOTA OBTIDA EM CADA COLUNA:")
for valor in maiores_valores:
    print(f"{valor:.1f}")

#printa o resultado da média geral da turma C
print(" ")
print(f"A média geral da turma foi: {media_geral:.2f}")