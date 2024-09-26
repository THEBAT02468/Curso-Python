numeros = [2, 4, 1, 4, 6, 72, 344]

# numeros.sort(reverse=True)#ordena de forma descendente
numeros2 = sorted(numeros)  # ordena los numeros
numeros2 = sorted(numeros, reverse=True)  # ordena los numeros

print(numeros)
print(numeros2)

usuarios = [  # [4, "Chanchito"],
    # [1, "felipe"],
    # [5, "pulga"]
    # no se va a ordenar debido que se necesito que e primer valor sea algo contrable
    ["Chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]


# def ordena(elemento):
#    return elemento[1]


# usuarios.sort(key=ordena, reverse=True)
usuarios.sort(key=lambda el: el[1], reverse=True)

print(usuarios)
