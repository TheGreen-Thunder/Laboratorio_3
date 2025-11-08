def Espiral_Aurea():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

print(list(Espiral_Aurea()))
