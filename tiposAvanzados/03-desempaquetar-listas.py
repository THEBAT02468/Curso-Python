numeros = [1, 2, 3]

# esto es mierda PURA Y DURA!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
primero, *otros = numeros

print(primero, segundo, tercero)
print(primero, otros)
