media = float(input("Digite a média de suas notas: "))
faltas = int(input("Digite o seu numero de faltas: "))

if media >= 7 and faltas < 32:
    print("APROVADO")
elif media < 7 and faltas >=32:
    print("REPROVADO por média e por faltas")
elif media < 7 or faltas >=32:
    print("REPROVADO por média ou por faltas")