#dicionarios, listas e variaveis
alunos = {}
medias = {}
reprovados = {}
aprovados = {}
somatorio_turma = 0

#repetição para pegar os dados
for i in range(0, 3):
    matricula = int(input("Digite sua matricula: "))
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    print("\n")
    media = (nota1+nota2)/2
    somatorio_turma += media
    media_turma = somatorio_turma/3
#salvar os alunos que estão reprovados e aprovados
    if media <= 5:
        reprovados.update({matricula: media})
    else:
        aprovados.update({matricula: media})
"""
Salvar todos os alunos com suas notas e suas respectivas médias
Não está sendo utilizado
    alunos.update({matricula: (nota1, nota2)})
    medias.update({matricula: media})
"""
#mostrar os resultados em tela
print("TOTAL DE ALUNOS APROVADOS: {}".format(len(aprovados)))
for matricula, media in aprovados.items():
    print("Aluno com matrícula: {}, obteve média: {:.2f} e está APROVADO".format(matricula, media))
print("\n")

print("TOTAL DE ALUNOS REPROVADOS:  {}".format(len(reprovados)))
for matricula, media in reprovados.items():
    print("Aluno com matrícula: {}, obteve média: {:.2f} e está REPROVADO".format(matricula, media))

print("\n")
print("A MÉDIA DE TODA TURMA FOI: {:.2f}".format(media_turma))