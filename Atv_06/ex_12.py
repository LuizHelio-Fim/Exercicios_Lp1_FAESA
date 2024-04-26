sexos = []
alturas = []
alturasF = []
idades = []
alturasF30 = 0
tot_entradas = 0

for i in range(0, 5):
    sexo = str(input("Qual o seu sexo, M para homem ou F para mulher: ")).upper()
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    alturas.append(altura)
    alturas.sort(reverse=True)

    if sexo == "F" and altura >= 1.7:
        alturasF.append(altura)
    
    if sexo == "F" and idade > 30:
        alturasF30 += altura
        tot_entradas += 1

    
media = alturasF30/tot_entradas

print("A maior altura inserida foi: {}".format(alturas[0]))
print("O numero de mulheres que tem mais de 1.7m é: {}".format(len(alturasF)))
print("A media das alturas das mulheres com mais de 30 anos é: {:.2f}".format("media"))
        