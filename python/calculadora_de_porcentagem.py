def repetir():
    print("descubra a porcentagem de um valor:")

    valor_inicial = int(input("digite o valor: "))

    porcentagem = int(input("agora digite a porcentagem: "))

    operacao = porcentagem * valor_inicial /100

    print("esse eh o resultado", operacao)

    pergunta = input("\ndesejar continuar? (sim/não) ").lower()
    return pergunta

while True:
    repetição = repetir()
    if repetição != "sim":
        break
