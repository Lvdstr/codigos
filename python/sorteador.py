import random
i = int(input("quantos personagens deseja sortear:"))
for x in range(i):
    with open('txt/chars.txt', 'r') as arquivo:
        lista_de_itens = arquivo.read().splitlines()
    item_sorteado = random.choice(lista_de_itens)
    print(f"O personagem sorteado é: {item_sorteado}")
