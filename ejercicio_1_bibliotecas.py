# solicitar paises separados por coma

paises = input("Ingrese una lista de paises (separe con comas): ")

# almacenar paises en una lista

paises_como_lista = paises.split(",")

# dejar solo elementos no repetidos en lista

paises_no_repetidos = list(paises_como_lista)

# ordenar alfabeticamente

paises_no_repetidos.sort(reverse=False)

print(paises_no_repetidos)