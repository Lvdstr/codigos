import random
confirmação = ["sim", "Sim", "SIM", "s", "S"]
    
def repetir():
    print("esse programa python oferece algumas funções relacionadas a pokémon")
    question = int(input("""
aqui estão as opções disponíveis
1 = realizar um sorteio de pokemons
2 = abrir a lista de pokemons para visualização e/ou modificação
"""))
    
    if question == 1:
        inicial = int(input("quantos pokemons vai querer sortear: "))
        for x in range(inicial):
            with open('txt/gen1 até gen5.txt', 'r') as arquivo:
                lista_de_itens = arquivo.read().splitlines()
            item_sorteado = random.choice(lista_de_itens)
            print(f"O pokemon sorteado é: {item_sorteado}")
            
    elif question == 2:
            r = open('txt/gen1 até gen5.txt', 'r')
            print(r.read())
            r.close()
            a = input("deseja fazer alterações no arquivo?")
            if a in confirmação:
                r = open('txt/gen1 até gen5.txt', 'a')
                write = input("digite um novo pokemon para adicionar ao arquivo:")
                ql = "\n"
                r.write(ql + write)
                r = open('txt/gen1 até gen5.txt', 'r')
                print(r.read())
                r.close()
            
            else:
                print("blz")
                r.close()
            
    pergunta = input("""
desejar repetir o código?
sim,Sim, SIM, s, S todas essas respostas são consideradas validas para recomeçar o código
e qulaquer resposta diferente disso é considerado não
""")
    return pergunta

while True:
    resposta = repetir()
    if resposta not in confirmação:
        print("aqui é o fim do código")
        break
