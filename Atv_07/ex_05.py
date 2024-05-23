import random
import string

#gerar sempre letras aleatórias
vetor_letras = [random.choice(string.ascii_letters) for _ in range(80)]

#ver se tem letras A presentes e se tiver fornecer a quantidade
letras_a = vetor_letras.count('A') + vetor_letras.count('a')
if letras_a == 0:
    print("Não existe nenhuma letra A na lista.")
else:
    print(f"A letra 'A' apareceu {letras_a} vez(es) no vetor.")

#conferir se existem pares de letras seguidas 
pares = []
cont_pares = 0
for i in range(len(vetor_letras) - 1):
    if vetor_letras[i] == vetor_letras[i+1]:
        pares.append(vetor_letras[i])
        cont_pares += 1

if cont_pares > 0:
    print(f"A(s) letra(s): {pares}, aparecem uma após a outra, isso acontece {cont_pares} vez(es).")
else:
    print("Não há letras sequenciais aparecendo")