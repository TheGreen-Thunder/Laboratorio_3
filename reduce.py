from functools import reduce

suma = reduce(lambda a,b: a+b, [5,10,15,20])
producto = reduce(lambda a,b: a*b, [2,3,4])
mayor = reduce(lambda a,b: a if a > b else b, [7,3,9,1,5])
concatenar = reduce(lambda a,b: a + b, ["Hola", " ", "Mundo", "!"])

print(suma)
print(producto)
print(mayor)
print(concatenar)