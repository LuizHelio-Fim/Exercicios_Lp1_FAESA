from random import randint

#preenche a matriz com numeros aleatórios e depois procura o maior elemento da matriz e suas posições
maior = 0
matriz = []
tamanho = 4
posicoes = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        n = randint(1, 10)
        if n > maior: #acha o maior numero, comeã uima nova lista de posições
            posicoes = [(i, j)]
            maior = n
        elif n == maior: #igual ao maior, adiciona a posição na lista
            posicoes.append((i, j))
        linha.append(n)
    matriz.append(linha)

print(matriz)
print("Maior numero: ", maior)
print("Posições do maior numero: ", posicoes)