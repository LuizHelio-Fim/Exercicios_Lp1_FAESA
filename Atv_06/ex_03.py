i = 0
soma = 0
cont = 0
while i != -1:
    i = int(input("Digite numeros(-1 para parar): "))
    soma = soma + i
    cont += 1

soma_final = soma + 1
media = soma_final/cont

print(media)