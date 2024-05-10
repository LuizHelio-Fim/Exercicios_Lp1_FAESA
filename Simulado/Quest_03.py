
prof = ""
idade_Tot = 0
medicos = 0
i = None

while i != 0:
    i = int(input("Digite sua idade: "))
    prof = input("Digite sua profissão: ").lower()

    if prof == "medico":
        idade_Tot += i
        medicos += 1

if medicos == 0:
    print("Não existe ninguem com a profissão de médico")
else:
    media_medicos = idade_Tot/medicos
    print(f"Existem: {medicos} médicos")
    print("A média de todas as idades dos médicos é: {:.2f}".format(media_medicos))