inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"\nNúmeros de Armstrong entre {inicio} e {fim}:")

for n in range(inicio, fim + 1):
    ordem = len(str(n))  # quantidade de dígitos
    soma = 0
    temp = n
    
    while temp > 0:
        digito = temp % 10
        soma += digito ** ordem
        temp //= 10

    if soma == n:
        print(n)