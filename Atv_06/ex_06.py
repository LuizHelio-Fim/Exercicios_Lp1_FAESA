maior_altura =  0
while True:
    altura = float(input("Digite a altura (0 para sair): "))

    if altura == 0:
        break
    if altura > maior_altura:
        maior_altura = altura

print(maior_altura)