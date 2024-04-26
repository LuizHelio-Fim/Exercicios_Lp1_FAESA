pontuacao_a = float(input("Informe a pontuação do Competidor A: "))
pontuacao_b = float(input("Informe a pontuação do Competidor B: "))
pontuacao_c = float(input("Informe a pontuação do Competidor C: "))
pontuacoes = [pontuacao_a, pontuacao_b, pontuacao_c]

pontuacoes.sort(reverse=True)

print("1º lugar: {} pontos".format(pontuacoes[0]))
print("2º lugar: {} pontos".format(pontuacoes[1]))
print("3º lugar: {} pontos".format(pontuacoes[2]))
