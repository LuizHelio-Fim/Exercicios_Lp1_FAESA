num = int(input("Fatorial de: "))
fat = 1
cont = 1

while cont <= num:
    fat *= cont
    cont += 1

print(fat)