salario = float(input("Digite seu salário: "))
financ = float(input("Digite o quanto quer finacear: "))

if financ <= 5*salario:
    print("Financeamento Concedido")
else:
    print("Financeamento Negado")
print("Obrigado por nos consultar.")