print("Bienvenido a un intento de calculadora XD")
print("Para salir escribir salir")
operacion = ""
print("las operaciones son suma, resta, multiplicacion")
numero = ""
while True:
    if not numero:
        numero = input("Ingrese número: ")
        if numero.lower() == "salir":
            print("gracias vuelva pronto")
            break

        numero = int(numero)

        operacion = input(
            "escoja una operacion las cuales son: suma, rest, div, multi: ")

        if operacion.lower() == "salir":
            print("gracias vuelva pronto")
            break

        numero2 = input("Ingresa un segundo numero: ")

        if numero2.lower() == "salir":
            print("gracias vuelva pronto")
            break
        numero2 = int(numero)

        if operacion.lower() == "suma":
            numero = numero+numero2
            print("la suma es: ", numero)
            break
        elif operacion.lower() == "rest":
            numero2 = int(input("Ingresa un segundo numero: "))
            numero = numero-numero2
            print("la resta es: ", numero)
            break
        elif operacion.lower() == "div":
            numero2 = int(input("Ingresa un segundo numero: "))
            numero = numero/numero2
            print("la division es: ", numero)
            break
        elif operacion.lower() == "multi":
            numero2 = int(input("Ingresa un segundo numero: "))
            numero = numero*numero2
            print("la multiplicasion es: ", numero)
            break
        else:
            print("datos no validos")
            break
