lista = [1, 2, 3, 4]
# print(1, 2, 3, 4)
# print(*lista)

lista2 = [5, 6]

combinada = ["hola", *lista, "mundo", *lista2]
print(combinada)

punto1 = {"X": 13, "Y": "hola"}
punto2 = {"Y": 45}

nuevoPunto = {**punto1, **punto2, "Z": "hola"}
print(nuevoPunto)
