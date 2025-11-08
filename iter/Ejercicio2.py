class NumerosImpares:
    def __iter__(self):
        for i in range(1, 21):
            if i % 2 != 0:
                yield i

for x in NumerosImpares():
    print(x)
