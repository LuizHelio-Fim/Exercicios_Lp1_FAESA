letra = None
letras_a = 0

while letra != str(0):
    letra =  input("Digite alguma letra: ").lower()

    if letra == "a":
        letras_a += 1

if letras_a > 0:
    print(f"a letra 'a' foi digitada {letras_a} vezes!")
else:
    print("A letra 'a' não foi digitada nenhuma vez!")