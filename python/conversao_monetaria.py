print("conversor de moedas")
escolha = input("primeiro deseja converter dolar ou real?").lower()

if escolha.isalpha() == False:
  print("nao vai não em")

elif escolha.isalpha() == True:
  if escolha == "dolar":
    dolar = int(input("digite o valor para converter: "))
    conversão = dolar * 5
    print(f"{dolar} dolar/es convertido/s para real da {conversão} real/ais")
    
  elif escolha == "real":
    real = int(input("digite o valor para converter: "))
    conversão = real / 5
    print(f"{real} real/ais convertido/s para dolar da {conversão} dolar/es")
