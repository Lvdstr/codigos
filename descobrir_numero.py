"""
atualizações:
1-adicionar outro input que pergunte até que numero vai ser a adivinhação
2-quanto maior for o numero pra adivinhar maior o numero de chance
3- e acrescentar uma palavra para parar o programa tipo um * ja que o input é do tipo int vai provavelmente gerar um erro ao colocar uma string

"""
import random
numero = random.randrange(1, 10)
chance = 5

print("adivinhe o numero correto")
while True:
  palpite = int(input("digite um numero: "))
  if palpite != numero:
    chance -= 1
    print("numero errado")
    palpite = int(input("tente de novo: "))
    print(f"{chance} restante/s")
    
  elif palpite == numero:
    print("tu acertou")
    print(f"{numero} é o numero correto")
    break
  
  if chance == 0:
    break
  
