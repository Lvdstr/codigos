operações = ["+", "-", "*", "/", "%", "//", "**"]
yes = ["Sim", "SIM", "sim", "S", "s", "yes", "y", "Y"] 
chance = 4
def repetir():
  global chance
  print("calculazinha")
  numero_1 = input("digite o primeiro valor: ")
  numero_2 = input("digite o segundo valor: ")
  while numero_1 == "" and numero_2 == "":
      print("parece que ocorreu um erro de digitação,tente dnv")
      numero_1 = input("digite o primeiro valor: ")
      numero_2 = input("digite o segundo valor: ")
      print(" ")
    
  numero_1 = int(numero_1)
  numero_2 = int(numero_2)

  operacao = input('''
escolha a operacao
+ para adicao
- para subtracao
* para multiplicacao
/ para divisao
% para modulo
// para divisao minima
** para exponencial
''')

  while operacao not in operações:
    operacao = input("por favor escolha uma das operações validas: ")
    print(f"ainda resta/m {chance} tentativa/s")
    chance -= 1
   
    if chance == 0:
      print("cabo a patifaria kkkk")
      return
    
  if operacao == '+':
    print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
    
  elif operacao == '-':
    print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
    
  elif operacao == '*':
    print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
    
  elif operacao == '/':
  	if numero_1 == 0 or numero_2 == 0:
  		print("não é possível dividir por zero irmão")
  	else:
  		print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
    
  elif operacao == '%':
    print(f"{numero_1} % {numero_2} = {numero_1 % numero_2}")
      
  elif operacao == '//':
    print(f"{numero_1} // {numero_2} = {numero_1 // numero_2}")

  elif operacao == '**':
    print(f"{numero_1} ** {numero_2} = {numero_1 ** numero_2}")

  repeat = input("\ndesejar continuar? (sim/não) ").lower()
  return repeat

while True:
    verificar = repetir()
    if verificar not in yes:
        break
