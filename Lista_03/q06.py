import random

num = random.randint(1, 9)

print("Tente adivinhar o número entre 1 e 9!")
print("Digite 'sair' para encerrar o jogo.\n")

while True:
    palpite = input("Seu palpite: ")

    if palpite.lower() == "sair":
        print("Jogo encerrado!")
        break


    palpite = int(palpite)

    if palpite < num:
        print("Muito baixo!")
    elif palpite > num:
        print("Muito alto!")
    else:
        print("Parabéns, você acertou!")
        break
