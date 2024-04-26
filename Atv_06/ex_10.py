fib_sequence = [0, 1]
n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
   print("Por favor, digite um número inteiro positivo.")
else:
   while len(fib_sequence) < n:
      proximo_termo = fib_sequence[-1] + fib_sequence[-2]
      fib_sequence.append(proximo_termo)

   print(*fib_sequence)