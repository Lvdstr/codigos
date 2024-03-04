yes = ["Sim", "SIM", "sim", "S", "s", "yes", "y", "Y"]
def repetir():
    print("Calcule o valor de um produto com desconto")
    
    valor = float(input("Informe o valor do produto: "))
    desconto = float(input("Informe a porcentagem de desconto: "))
    
    valor_com_desconto = valor - (valor * desconto / 100)
    
    print(f"Esse é o valor do produto com desconto: {valor_com_desconto}$ reais")
    
    pergunta = input("Continuar calculando? (sim/não): ")
    return pergunta

while True:
    pergunta = repetir()
    if pergunta.lower() not in yes:
        break
