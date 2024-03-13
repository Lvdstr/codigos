import random

number = 0
pergunta = int(input("digite quantos numeros vai querer gerar"))
if pergunta == 0:
	print("a quantidade de numeros geradas sera aleatória")
	pergunta = random.randrange(1, 10)
	print(" ")
print("""
agora escolha um numero,apos isso sera
gerado aleatoriamente um numero no
intervalo de 1 ate o numero digitado
""")
print(" ")
for i in range(pergunta):
	number += 1
	stop = int(input("escolha um numero: "))
	print(f"o {number} numero eh:", random.randint(1, stop))
	print("pronto! o programa foi encerrado")
