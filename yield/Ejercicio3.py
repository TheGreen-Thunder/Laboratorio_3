class CuadradoNumeros:
    def __iter__(self):
        for i in range(1, 11):
            yield i * i

for x in CuadradoNumeros():
    print(x)
