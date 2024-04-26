idade = int(input("Informe sua idade: "))

if idade > 5:
    if idade >= 5 and idade <= 7:
        categoria = "Infantil A"
    elif idade >= 8 and idade <= 11:
        categoria = "Infantil B"
    elif idade >= 12 and idade <= 13:
        categoria = "Juvenil A"
    elif idade >= 14 and idade <= 17:
        categoria = "Juvenil B"
    elif idade >= 18:
        categoria = "Adulto"

    print("Categoria: {}".format(categoria))
else:
    print("Menores que 5 anos não são classificados")