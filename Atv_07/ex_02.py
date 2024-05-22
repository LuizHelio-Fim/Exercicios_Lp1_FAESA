numeros = []
numerosATerceira = None
numeros_elevados = []

while True:
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        numeros.append(numero) 
    if len(numeros) == 100:
        break

for i in range(0, 100):
    numerosATerceira = numeros[i]
    numeros_elevados.append(pow(numerosATerceira, 3))

print(numeros_elevados)