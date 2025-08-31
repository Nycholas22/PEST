soma = 0
for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        soma += n
print("a soma dos números primos entre 1 e 100 é:", soma)
