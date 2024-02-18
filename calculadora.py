lista = ["+", "-", "*", "/", "%", "//", "**"]
def calculo(opção):
    if opção == 1:
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
        
        while operacao not in lista:
            operacao = input("por favor escolha uma das operações validas: ")
        
        numero_1 = int(input("digite o primeiro valor: "))
        numero_2 = int(input("digite o segundo valor: "))
        
        if operacao == '+':
            print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
        
        elif operacao == '-':
            print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
        
        elif operacao == '*':
            print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
        
        elif operacao == '/':
            print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
        
        elif operacao == '%':
            print(f"{numero_1} % {numero_2} = {numero_1 % numero_2}")
        
        elif operacao == '//':
            print(f"{numero_1} // {numero_2} = {numero_1 // numero_2}")

        elif operacao == '**':
            print(f"{numero_1} ** {numero_2} = {numero_1 ** numero_2}")


print("""
bem vindo ah calculadora master! um projeto de calculadora que oferece diversas calcluadoras
integrados numa só,aqui estão as calculadoras disponiveis:
1-calculadora padrão
""")
pergunta = int(input("escolha umas das calculadoras para usar: "))
calculo(pergunta)
