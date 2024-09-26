numero = (1, 2, 3) + (4, 5, 6)
print(numero)

punto = tuple([1, 2])

print(punto)

menosNumeros = numero[:2]

print(menosNumeros)

primero, segundo, *otros = numero
print(primero, segundo, otros)

for n in numero:
    print(n)

listaNumero = list(numero)
listaNumero[0] = "Hola"
print(listaNumero)
