class IterEnMayusculas:
    def __init__(self, lista):
        self.lista = lista

    def __iter__(self):
        for palabra in self.lista:
            yield palabra.upper()

for palabra in IterEnMayusculas(["hola", "mundo", "python"]):
    print(palabra)
