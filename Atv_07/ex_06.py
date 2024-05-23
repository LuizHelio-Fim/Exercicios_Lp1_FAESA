# Lista de produtos
produtos = [
    "Macarrão", "Arroz", "Feijão", "Açúcar", "Sal", "Café", "Óleo", "Farinha", "Leite", "Manteiga",
    "Pão", "Ovos", "Carne", "Frango", "Peixe", "Queijo", "Presunto", "Iogurte", "Suco", "Refrigerante",
    "Biscoito", "Chocolate", "Sorvete", "Pizza", "Batata", "Cenoura", "Tomate", "Alface", "Cebola", "Alho",
    "Maçã", "Banana", "Laranja", "Pera", "Uva", "Manga", "Melancia", "Abacaxi", "Morango", "Limão",
    "Sabão", "Detergente", "Amaciante", "Desinfetante", "Shampoo", "Condicionador", "Creme Dental", "Sabonete", "Papel Higiênico", "Guardanapo",
    "Esponja", "Saco de Lixo", "Velas", "Fósforos", "Pilha", "Lâmpada", "Vassoura", "Rodo", "Pá de Lixo", "Pano de Chão",
    "Saco Plástico", "Filme PVC", "Papel Alumínio", "Prato Descartável", "Copo Descartável", "Talher Descartável", "Guardanapo de Papel", "Toalha de Papel", "Fita Adesiva", "Cola",
    "Lápis", "Caneta", "Borracha", "Apontador", "Caderno", "Livro", "Revista", "Jornal", "Envelope", "Cartolina",
    "Tinta", "Pincel", "Corda", "Fio de Nylon", "Parafuso", "Prego", "Martelo", "Chave de Fenda", "Alicate", "Serra",
    "Furadeira", "Lixa", "Verniz", "Tinta Spray", "Balde", "Mangueira", "Regador", "Adubo", "Sementes", "Muda de Planta"
]

# Lista de quantidades
quantidades = [
    50, 100, 75, 80, 45, 60, 30, 55, 70, 40,
    90, 120, 35, 65, 25, 50, 30, 40, 85, 100,
    110, 55, 70, 45, 60, 85, 90, 30, 25, 40,
    100, 80, 75, 60, 95, 70, 40, 50, 35, 65,
    30, 55, 60, 45, 70, 75, 40, 35, 90, 60,
    30, 50, 45, 65, 70, 80, 35, 55, 75, 100,
    60, 40, 35, 55, 75, 90, 50, 45, 70, 60,
    80, 55, 40, 50, 35, 45, 75, 60, 55, 90,
    50, 70, 80, 60, 40, 55, 75, 65, 35, 50,
    70, 90, 40, 55, 30, 45, 35, 65, 55, 70
]

# Lista de preços
precos = [
    4.50, 3.20, 5.00, 2.80, 1.50, 6.40, 7.20, 2.50, 3.10, 8.40,
    5.50, 4.30, 10.00, 8.00, 12.50, 15.00, 20.00, 6.00, 5.20, 7.00,
    3.50, 4.50, 10.50, 8.80, 3.00, 2.50, 4.00, 3.20, 1.80, 1.00,
    2.20, 1.50, 1.80, 2.00, 3.50, 4.80, 2.80, 7.50, 5.00, 1.80,
    2.50, 3.00, 4.50, 5.00, 6.50, 7.00, 2.20, 1.00, 6.00, 2.80,
    1.50, 2.20, 1.80, 2.00, 3.00, 4.20, 2.80, 5.50, 7.50, 6.00,
    1.50, 2.80, 4.50, 5.00, 1.00, 1.20, 3.00, 2.80, 1.50, 2.00,
    1.80, 2.50, 3.00, 4.00, 5.50, 6.20, 7.00, 2.50, 1.20, 3.00,
    4.50, 5.20, 6.00, 2.80, 1.50, 3.20, 4.00, 5.50, 2.80, 3.00,
    4.50, 6.20, 2.00, 3.50, 1.80, 2.50, 3.00, 4.20, 2.50, 3.00
]
#valores gerados pelo chatGPT

#calcula o faturamento de cada produto separadamente
faturamento = []
for i in range(min(len(quantidades), len(precos))):
    fat = quantidades[i]*precos[i]
    faturamento.append(fat)

#mostra na tela todos os produtos e o faturamento de cada um deles
cont = 0
for i in produtos:
    print(f"mercadoria: {produtos[cont]}")
    print("Faturamento: R${:.2f}".format(faturamento[cont]))
    print(" ")
    cont += 1

#mostra na tela o faturamento total
print("O faturamento TOTAL foi de: R${:.2f}".format(sum(faturamento)))