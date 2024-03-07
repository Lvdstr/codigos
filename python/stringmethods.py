import time

lista = []
def convert_tipo(valor):
	if valor.isdigit() == False:
		opcao = int(input("""
pronto o valor foi recebido,e ele é do 
tipo string então abaixo esta um lista
de funções envolvendo strings,então 
escolha uma
1-todo o texto para minusculo
2-todo o texto para maiusculo
3-só a primeira letra em maiusculo
4-contar quantos caracteres tem no texto
agora escolha sua opção:"""))
		if opcao == 1:
			if valor.isdigit() == True:
				print("fatal error")
				print("o valor digitado não pode ser alterado por esse metodo")
				print("tentando dnv...")
				time.sleep(2)
				print("infelizmente não foi possivel concluir essa ação.programa encerrado")
				return
			else :
				valor = valor.lower()
				print(valor)
	
		elif opcao == 2:
			if valor.isdigit() == True:
				print("fatal error")
				print("o valor digitado não pode ser alterado por esse metodo")
				print("tentando dnv...")
				time.sleep(2)
				print("infelizmente não foi possivel concluir essa ação.programa encerrado")
				return
			else :
				valor = valor.upper()
				print(valor)
	
		elif opcao == 3:
			if valor.isdigit() == True:
				print("fatal error")
				print("o valor digitado não pode ser alterado por esse metodo")
				print("tentando dnv...")
				time.sleep(2)
				print("infelizmente não foi possivel concluir essa ação.programa encerrado")
				return
			else:
				valor = valor.capitalize()
				print(valor)
	
		elif opcao == 4:
			if valor.isdigit() == True:
				print("fatal error")
				print("o valor digitado não pode ser alterado por esse metodo")
				print("tentando dnv...")
				time.sleep(2)
				print("infelizmente não foi possivel concluir essa ação.programa encerrado")
				return
			else:
				valor = len(valor)
				print(f"o tamnho do texo eh de: {valor} caracter/es")
	
	elif valor.isdigit() == True:
		valor = int(valor)
		print("""
pronto o valor foi recebido,e ele é do 
tipo inteiro então abaixo esta um lista
de funções envolvendo inteiros,então 
escolha uma
1 = fatorial do numero
2 = acresimo de porcentagem
3 = area do retângulo
4 = verificar maior e menor numero
5 = numero primo ou não""")
		opcao = int(input("agora escolha uma opção: "))
		if opcao == 1:
			fatorial = 1
			count = 1
			while count <= valor:
				fatorial *= count
				count += 1
				print(fatorial)
      
		elif opcao == 2:
			print("o primeiro valor foi a porcentagem")
			value = int(input("agora o valor: "))
			initial, divided = valor, valor / 10
			union = initial + divided
			soma = value * union
			print(soma)
      

		elif opcao == 3:
			altura = int(input("o primeiro foi a base agora digite a altura:"))
			area = valor * altura
			print(f"a area do retangulo eh {area}")
      
		elif opcao == 4:
			for p in range(valor):
				lis = int(input("digite os numeros: "))
				lista.append(lis)
			menor = min(lista)
			maior = max(lista)
			print(f"maior numero:{maior} \nmenor numero:{menor}")


		elif opcao == 5:
			if valor > 1:
				for x in range(2, valor):
					if (valor % x) == 0:
						print("esse não eh primo")
						break
					else:
						print("esse numero eh primo")
			else:
				print("esse numero eh menor ou igual 1")
				