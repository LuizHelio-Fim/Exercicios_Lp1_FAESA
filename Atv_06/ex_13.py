alturas = []
alturas_maiores = []
alturas_menores = []
for i in range(0, 5):
    altura = float(input("Insira sua altura: "))
    alturas.append(altura)
    alturas.sort()

    if altura > 1.6:
        alturas_maiores.append(altura)
    elif altura < 1.3:
        alturas_menores.append(altura)

media = (alturas[0] + alturas[4])/2

print("\n")
print("A maior altura é : {}".format(alturas[4]))
print("A menor altura é: {}".format(alturas[0]))
print("A media entre a maior e a menor altura é: {:.2f}".format(media))
print("------------------------------------")
print("{} pessoas tem altura maiores que 1.60m".format(len(alturas_maiores)))
print("{} pessoas tem altura menores que 1.30m".format(len(alturas_menores)))