altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/(pow(altura, 2))

if imc < 20:
    print("Abaixo do peso")
elif imc < 25:
    print("Normal")
elif imc < 35:
    print("Excesso de peso")
elif imc < 50:
    print("Obesidade")
else:
    print("Obesidade Mórbida")