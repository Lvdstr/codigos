vogal = "aeiou"
consoante = "bcdfghjklmnpqrstvwxyz"

print("Verifique se a letra digitada é uma vogal ou consoante")

while True:
    pergunta = input("Digite uma letra: ").lower()

    if pergunta.isalpha():
        if pergunta in vogal:
            print(f"{pergunta} é uma vogal")
            
        elif pergunta in consoante:
            print(f"{pergunta} é uma consoante")
        break
    else:
        print(f"{pergunta} não é uma letra")
