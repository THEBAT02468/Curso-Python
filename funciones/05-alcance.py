saludo = "hola global"


def saludar():
    global saludo  # mala practica
    saludo = "hola mundo"


def saludaSan():
    saludo = "hola san"
    print(saludo)


print(saludo)
saludar()
print(saludo)
# saludaSan()
# saludar()
