import os
from random import randint

print("descubra a senha digitada")
senha_digitada = input("Digite uma senha: ").lower()
characters = '123456789abcdefghijklmnopqrstuvwxyz'  # Caracteres usados na senha

senha_encontrada = ''
tentativas = 0  # Variável para contar as tentativas

while senha_encontrada != senha_digitada:
    senha_encontrada = ''
    tentativas += 1

    for _ in range(len(senha_digitada)):
        guess_senha_encontradad = characters[randint(0, len(characters) - 1)]
        senha_encontrada = guess_senha_encontradad + senha_encontrada
        print(f"Tentativa {tentativas}: {senha_encontrada}")

        # Descomente a linha abaixo se você estiver executando no Windows
        # os.system("clpolicias")

print(f"\nSenha encontrada após {tentativas} tentativas: {senha_encontrada}")