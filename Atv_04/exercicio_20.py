def produtos_reabastecer(produtos):
    reabastecer = []
    for produto in produtos:
        nome, estoque_atual, estoque_minimo = produto
        if estoque_atual < estoque_minimo:
            reabastecer.append(nome)
    return reabastecer

# Exemplo de entrada (Pode ser tirado de uma planilha do excel ou do banco de dados do mercado)
produtos = [("Arroz", 15, 20), ("Feijão", 10, 25), ("Óleo", 30, 40), ("Macarrão", 20, 15)]

print(produtos_reabastecer(produtos))
