matriculas = []
funcionarios = {}
somatorio_salarial = 0

while True:
    matricula = int(input("Forneça seu numero de matricula: "))
    if matricula == 0:
        break
    salario_dia = float(input("Forneça seu salário por dia: R$"))
    numDias_trabalhados = int(input("Forneça a quantidade de dias trabalhados: "))

    matriculas.append(matricula)
    salario = salario_dia*numDias_trabalhados
    funcionarios.update({matricula: salario})
    
    somatorio_salarial += salario

media_salarial = somatorio_salarial/len(matriculas)

print("-------------------------------")
for matricula, salario in funcionarios.items():
    print("MATRICULA: {}".format(matricula))
    print("SALARIO: R${}".format(salario))
    print("-------------------------------")

print("O total de salários a serem pagos é: {}".format(len(matriculas)))
print("A media salárial é de: R${:.2f}".format(media_salarial))