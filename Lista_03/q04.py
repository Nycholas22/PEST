num = int(input("Digite um número\ 0 para sair: "))

while num != 0:
    print(f"divisores de {num}:")

divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print(divisor)
    divisor += 1

    num = int(input("Digite um número (0 para sair): "))
print("Programa encerrado.")
