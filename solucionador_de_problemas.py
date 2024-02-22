yes = ["Sim", "SIM", "sim", "S", "s", "yes", "y", "Y"]
no = ["Nao", "Não", "NÃO", "NAO", "NO", "No", "no", "n", "N"]
def repetir():
  print("solucionador de problemas")
  pergunta = input("a bagaça funciona:")
  if pergunta in yes:
    print("nem rela")
    print("sem problemas")
  else:
    pergunta_two = input("você que quebrou?")
    
    if pergunta_two in yes:
      print("seu imbecil")
      
      pergunta_three = input("alguém sabe que foi você?")
      
      if pergunta_three in no:
        print("esconda")
        print("sem problemas")
        
      elif pergunta_three in yes:
        print("se fodeu")
        pergunta_threee = input("da pra culpar alguém:")
        
        if pergunta_threee in yes:
          print("sem problemas")
          
        elif pergunta_threee in no:
          print("se fodeu")
          
    elif pergunta_two in no:
      pergunta_four = input("alguém pode te culpar?")
      
      if pergunta_four in yes:
        print("se fodeu")
        
        pergunta_five = input("ela tem provas reais contra vc?")
        
        if pergunta_five in yes:
          print("se fodeu")
          
        elif pergunta_five in no:
          print("tudo certo então")
          
      elif pergunta_four in no:
        print("então foda-se")
        print("sem problemas")
        
  pergunt = input('repetir código? ')
  return pergunt
while True:
  ap = repetir()
  if ap not in yes:
    break
