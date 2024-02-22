def repetir():
    print("realize o calculo da sua média")
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    nota3 = float(input("digite sua terceira nota: "))
    nota4 = float(input("digite sua quarta nota: "))
    media  = float((nota1 + nota2 + nota3 + nota4) /4)
    
    if media <= 3:
        print("sua nota éh I,você vai precisar ficar de recuperação")
    elif media <= 6:
        print("sua nota eh R,não de recuperação mas vai precisar estudar mais")
    elif media <= 9:
        print("sua nota eh B,ta estudando bem em mano")
    elif media == 10:
         print("sua nota eh MB,ta estudando muito em menó parabens")
    rp = input("\ndesejar repetir? (sim/não): ")
    return rp

while True:
    perguntinha = repetir()
    if perguntinha != "sim":
        break
        
