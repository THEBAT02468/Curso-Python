# and, or, not
gas = False
encendido = True
edad = 18
# if gas and encendido:
#   print("puedes avanzar")

# if gas or encendido:
#   print("puedes avanzar")
# if gas and encendido and edad > 17:
#   print("puede avanzar")
# operaciones corto circuito
if not gas or encendido or edad > 17:
    print("puede avanzar")
