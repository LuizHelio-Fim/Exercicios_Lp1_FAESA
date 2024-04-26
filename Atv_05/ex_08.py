salario = float(input("Informe o seu salário: "))

if salario < 500:
    reajuste = 0.15*salario

elif salario >=500 and salario<=1000:
    reajuste = 0.10*salario

else:
    reajuste = 0.05*salario

salario_novo = reajuste + salario

print("Salário antigo: R${:.2f}\nSalário Pós Reajuste: R${:.2f}".format(salario, salario_novo))