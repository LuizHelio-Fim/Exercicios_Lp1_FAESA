reta1 = float(input("Digite o primeiro segmento: "))
reta2 = float(input("Digite o segundo segmento: "))
reta3 = float(input("Digite o terceiro segmento: "))

if reta1 > reta2 + reta3 or reta3 > reta1 + reta2 or reta2 > reta1 + reta3:
    print("Não é possivel formar um triangulo")
elif reta1 == 0 or reta2 == 0 or reta3 == 0:
    print("Não é possivel formar um triangulo")
else:
    if reta1 == reta2 == reta3:
        print("Triangulo equilátero")
    elif reta1 != reta2 != reta3 != reta1:
        print("Triangulo escaleno")
    else:
        print("Triangulo Isósceles")