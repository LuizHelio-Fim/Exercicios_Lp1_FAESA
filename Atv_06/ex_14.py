num_calcados = int(input("Quantos calçados vai levar: "))
preco_calcado = 0
i = 1

while i <= num_calcados:
    preco_calcado += 49.90
    i+=1

if num_calcados <=2:
    desconto = 0.05*preco_calcado
else:
    desconto = 0.15*preco_calcado

valor_final = preco_calcado - desconto

print("O valor final da compra ficou em: R${:.2f}".format(valor_final))