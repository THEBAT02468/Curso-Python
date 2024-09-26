animal = " gaTO m "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.capitalize())
print(animal.strip())
print(animal.lstrip())
print(animal.title())
print(animal.rstrip())
print(animal.find("gA"))  # no encontro en el string si da -1
# pasamos una parte del stign a reemplazar y de ahi por cual otro string reemplazo
print(animal.replace("aTO", "jo"))
print("aTO" in animal)  # para saber si hay un caracter en el string
print("aTO" not in animal)  # para saber si no hay un caracter en el string
