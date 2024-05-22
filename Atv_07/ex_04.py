numeros = []

for i in range(0, 10):
    numeros.append(int(input("Digite um numero: ")))

maior_numero = max(numeros)
print("O maior numero digitado é: " , maior_numero , "e sua posição na lista é: " , numeros.index(maior_numero) + 1)

