#variaveis while
cont = 0
i = 0
valores_negativos = 0
valores_positivos = 0

# receber os valores da média e separar os positivos dos negativos

while True:
    num = int(input("Forneça os valores: "))
    i += num
    cont += 1
    if num < 0:
        valores_negativos += 1
    elif num > 0:
        valores_positivos += 1
    else:
        break

media = i/cont
perc_negativo = valores_negativos*100
perc_negativo_final = perc_negativo/cont

print("Média dos valores fornecidos: {:.2f}".format(media))
print("Quantidade de valores positivos: {}".format(valores_positivos))
print("Percentual de valores negativos: {:.2f}%".format(perc_negativo_final))