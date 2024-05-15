opn_boa = 0
opn_ruim = 0
opn_total = 0

while True:
    print("O que você achou do filme?")
    print("BOM\nRUIM")
    opn = input(">").upper()
    print("\n")

    if opn == "BOM" or opn == "RUIM":
        if opn == "BOM":
            opn_boa += 1
        elif opn == "RUIM":
            opn_ruim += 1

        opn_total += 1
    else:
        print("Digite apenas BOM ou RUIM!")
        continue
    if opn_total == 15:
        break

print(f"Opiniões totais: {opn_total}")
print(f"Opiniões Boas: {opn_boa}")
print(f"Opiniões Ruins: {opn_ruim}")