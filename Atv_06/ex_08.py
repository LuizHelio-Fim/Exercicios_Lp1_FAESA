#Declaração de variaveis
votos = 0
candidatoUm = 0
candidatoDois = 0
candidatoTres = 0
votoNulo = 0
votoBranco = 0
res = 0

#Estrutura de repetição para votação
while res != -1:
    print("1 - Candidato Umberto")
    print("2 - Candidato Doisberto")
    print("3 - Candidato Tresberto")
    print("4 - Voto Nulo")
    print("0 - Voto Branco")
    print("\n")
    res = int(input("Insira o valor (-1 para sair):"))
    
    #adicionar votos
    match res:
        case 1:
            candidatoUm += 1
        case 2:
            candidatoDois += 1
        case 3:
            candidatoTres += 1
        case 4:
            votoNulo += 1
        case 0:
            votoBranco += 1
        case _:
            print("Numero invalido")
            continue
    votos += 1
        
#ordenador os canditados com maior numero de pontos
candidatos = [candidatoUm, candidatoDois, candidatoTres]
candidatos.sort(reverse=True)

if candidatoUm > candidatoDois and candidatoUm > candidatoTres:
    candidatoVencedor = "Umberto"
elif candidatoDois > candidatoUm and candidatoDois > candidatoTres:
    candidatoVencedor = "Doisberto"
else:
    candidatoVencedor = "Tresberto"

print("O CANDIDATO VENCEDOR FOI: {} com {} votos".format(candidatoVencedor, candidatos[0]))
print("O Nº DE VOTOS BRANCOS FOI: {}".format(votoBranco))
print("O Nº DE VOTOS NULOS FOI: {}".format(votoNulo))
print("O Nº TOTAL DE ELEITORES QUE VOTARAM FOI: {}".format(votos))