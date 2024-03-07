from stringmethods import convert_tipo

yes = ["Sim", "SIM", "sim", "S", "s", "yes", "y", "Y"]

while True:
	pergunta = input("""por favor digite algo:""")
	convert_tipo(pergunta)
	
	continue_or_not = input("deseja continuar?:").lower()
	if continue_or_not not in yes:
		break
