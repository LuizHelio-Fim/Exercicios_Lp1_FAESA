pessoas = {}
mulheres_20 = []
soma_idade = 0

for i in range(0, 4):
    nome = str(input("Digite seu nome: ")).title()
    idade = int(input("Digite sua idade: "))
    print("Digite seu sexo: ")
    print("F - Mulher\nM - Homem\nO - outro")
    sexo = str(input("> ")).upper()

    pessoas[nome] = {'idade': idade, 'sexo': sexo}
    
    soma_idade += idade

    if sexo == "F" and idade < 20:
        mulheres_20.append(nome)

idade_media = soma_idade/4

nomes_formatados = ", ".join(mulheres_20)

mais_velho = None
idade_maxima = 0

for nome, dados in pessoas.items():
    if dados['idade'] > idade_maxima:
        mais_velho = nome
        idade_maxima = dados['idade']

print("A media das idades de todos foi: {}".format(idade_media))
print("{} é a pessoa mais velha com {} anos".format(mais_velho, idade_maxima))
print("As mulheres que tem menos de 20 anos são: {}".format(nomes_formatados))