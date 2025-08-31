inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"Números de Armstrong entre {inicio} e {fim}:")

for numero in range(inicio, fim + 1):
    n = 0
    temp = numero
    for i in range(1, numero + 1):
        if temp == 0:
            break
        temp = temp // 10
        n = n + 1

    soma = 0

    temp = numero
    for i in range(n):
        digito = temp % 10
        soma = soma + digito ** n
        temp = temp // 10

    if soma == numero:
        print(numero)
