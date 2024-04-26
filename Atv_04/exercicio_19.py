nome = input("Qual o seu nome?\n>")
salario = float(input("Qual o seu salário?\n>"))
vendas = float(input("Qual foi o seu total de vendas? (em dinheiro)\n>"))

comissao = 0.15*vendas
sal_final = salario + comissao

print("Olá {}\nSeu salário fixo é de: R${:.2f}\nSeu salário final é de: R${:.2f}".format(nome, salario, sal_final))