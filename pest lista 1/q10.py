N = int(input("Digite um número de quatro digitos: "))

d1 = N // 1000
d2 = (N // 100) - (N // 1000) * 10
d3 = (N // 10) - (N // 100) * 10
d4 = N - (N // 10) * 10

soma = d1 + d2 + d3 + d4
print(f"A soma dos dígitos é: {soma}")