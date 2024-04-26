nome = str(input("NOME: "))
nota_trab = float(input("Nota Trabalho: "))
nota_prova = float(input("Nota Prova:"))

media = (nota_prova + nota_trab)/2

if media > 7:
    print("\nNOME:{}\nSituação: APROVADO".format(nome))
else:
    print("\nNOME:{}\nSituação: REPROVADO".format(nome))