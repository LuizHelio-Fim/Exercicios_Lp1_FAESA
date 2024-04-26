i = 0
limiteDiario = float(input("Forneça em Kg o Limite: "))

while i < limiteDiario:
    pesoPeixe = float(input("Digite o peso do peixe (0 para sair): "))
    i += pesoPeixe
    print("Peso até o momento: {:.2f}Kg".format(i))

    if pesoPeixe == 0:
        break

if i > limiteDiario:
    print("Limite de {}Kg excedido!".format(limiteDiario))