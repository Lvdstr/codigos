print("calculo de probabilidades")
chances_possiveis = int(input("digite o numero de resultados desejados: "))
chances_totais = int(input("agora digite a quantidade maxima de resultados: "))
resultado = chances_possiveis / chances_totais
print(f'vc tem {resultado} % de chance em {chances_totais} tentativas')
