numeros = [1,2,3,4,5]
lista1 = list(map(lambda x: x * 10,  numeros))

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

palabras = ["uno","dos","tres"]
long = list(map(len, palabras))

cuadrados = list(map(lambda x: x*x, numeros))

print(lista1)
print(fahrenheit)
print(long)
print(cuadrados)