salarioBruto = float(input("Digite seu salário: "))
valorPrest = float(input("Digite o valor da prestação: "))

valorMax = 0.30*salarioBruto

if valorPrest > valorMax:
    print("Emprestimo Negado")
else:
    print("Emprestimo Concedido")