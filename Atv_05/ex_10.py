valor_hora = float(input("Quanto você recebe por hora aula?\n> "))
num_aulas = int(input("Quantas aulas você deu no mês?\n> "))
valor_INSS = float(input("Digite a % descontada pelo INSS:\n> "))

inss = valor_INSS/100
salario_inss = (valor_hora * num_aulas) * inss
salario = (valor_hora * num_aulas) - salario_inss
salario_minimo =  1412

if salario >= 10*salario_minimo:
    print("\nVocê recebe mais que 10 salários minimos, SORTUDO!\nSALARIO: {:.2f}".format(salario))
elif salario >= 6*salario_minimo:
    print("\nVocê recebe entre 6 e 9 salários minimos, Um dia você chega lá!!\nSALARIO: {:.2f}".format(salario))
else:
    print("\nVocê recebe menos de 6 salários minimos, Ah! Coitado!\nSALARIO: {:.2f}".format(salario))