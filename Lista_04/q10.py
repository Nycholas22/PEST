n = int(input("digite um número: "))
soma = 0

for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print("a soma dos números menores que {n} divisiveis por 3 ou 5 é:", soma)
