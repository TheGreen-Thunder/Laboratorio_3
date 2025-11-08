pares = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))

palabras = list(filter(lambda x: x.startswith("p"), ["perro","gato","pato","hamster"]))

mayores_que_50 = list(filter(lambda x: x > 50, [10,60,30,80,50,100]))

impares = list(filter(lambda x: x % 2 != 0, [1,2,3,4,5,6,7,8,9,10]))

print(pares)
print(palabras)
print(mayores_que_50)
print(impares)