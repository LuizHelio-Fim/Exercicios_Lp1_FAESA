cont = 0

soma = 0
for cont in range(0, 200):
    num = int(input("Digite o numero: "))
    res = num%3
    soma = soma + res

print(soma)