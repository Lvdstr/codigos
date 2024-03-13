def convert_type(valor):
    print("""
bem vindo esse modulo tem como função 
(kkkkkk) converter o tipo de dado de um
valor a seguir estão as conversões
disponiveis:
AVISO!!!
Uma string com valor numerico pode ser
convertida para outros tipos numericos
tranquilamente, e o contrario tambem mas
não tente converter uma string com
valor textual para tipos numéricos.
TIPOS DE DADOS PARA CONVERSÃO:
    1 = string
    2 = int
    3 = float
    4 = complex
    """)

    opcao = int(input("agora escolha uma opção:"))
    if opcao == 1:
      valor = str(valor)
      print(f"{valor} agora é uma string")
      print(type(valor))
        
    elif opcao == 2:
      if valor.isalpha() == True:
        return
      else:
        valor = int(valor)
        print(f'{valor} agora é um inteiro')
        print(type(valor))
        
    elif opcao == 3:
      if valor.isalpha() == True:
        return
      else:
        valor = float(valor)
        print(f'{valor} agora é um float')
        print(type(valor))
        
    elif opcao == 4:
      if valor.isalpha() == True:
        return
      else:
        valor = complex(valor)
        print(f'{valor} agora é um complex')
        print(type(valor))
        
    else:
      print("opção inválida")