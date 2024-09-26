def hola(nombre, apellido):  # parametro
    print("HOla mundo")
    print(f"Bienvenido {nombre}")


nombre = "santiago"
apellido = "lopez"
hola(nombre, apellido)  # argumento


def Hola(nombre, apellido="feliz"):  # parametro asignado
    print("HOla mundo")
    print(f"Bienvenido {nombre}")


Hola("sant", "apellido")
Hola("sant")
Hola(apellido="lopez", nombre="santiago")
