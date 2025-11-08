class ListaCuadrados:
    def obtener_cuadrados(self):
        return [i*i for i in range(1, 11)]

print(ListaCuadrados().obtener_cuadrados())
