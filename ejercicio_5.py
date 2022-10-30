# año_usuario = int(input("Escribe un año (numero entero): "))

# def biciesto(año):
#     if (año % 4) != 0:
#         resultado = "No es biciesto"
#     elif (año % 100) != 0:
#         resultado = "Es biciesto"
#     elif (año % 400) != 0:
#         resultado = "No es biciesto"
#     else:
#         resultado = "Es biciesto"
#     return resultado

# año_a_averiguar = biciesto(año_usuario)
# print(año_a_averiguar)

class padre:
	propiedad = True
	def metodo(self):
		self.propiedad = True


class hijo(padre):
    pass

h = hijo()
estado = h.metodo()
print(h.propiedad)
