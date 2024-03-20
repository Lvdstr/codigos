lista = []
def continha(valor):
    print("""
esse modulo oferece funções relacionadas
a numeros,a seguir confira as
opcoes disponiveis
escolha a opção que deseja:
1 = fatorial do numero
2 = acresimo de porcentagem
3 = area do retângulo
4 = verificar maior e menor numero
5 = numero primo ou não
""")
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
            
    else:
        print("opção inválida")