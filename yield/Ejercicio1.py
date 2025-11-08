def numeros_pares():
    for i in range(6):
        yield i * 2

for num in numeros_pares():
    print(num)