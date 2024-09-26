usuarios = [
    ["Chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

# nombres = []

# for usuario in usuarios:
#   nombres.append(usuario[0])
# print(nombres)
# nombres = [usuario[0] for usuario in usuarios]

# filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# map
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
