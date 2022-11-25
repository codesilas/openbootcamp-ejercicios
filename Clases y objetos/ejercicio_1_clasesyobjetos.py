class vehiculo():
    color = None
    ruedas = None
    puertas = None

    def asignar_color(self, a):
        self.color = a
        return self.color
    
    def cantidad_de_ruedas(self, a):
        self.ruedas = a
        return self.ruedas

    def cantidad_de_puertas(self, a):
        self.puertas = a
        return self.puertas

class coche(vehiculo):
    velocidad = None
    Cilindrada = None

    def cuanta_velocidad(self, a):
        self.velocidad = a
        return self.velocidad

    def asignar_cilindrada(self, a):
        self.Cilindrada = a
        return self.Cilindrada

myCoche = coche()

myCoche.asignar_color("verde")
myCoche.cantidad_de_puertas(2)
myCoche.cantidad_de_ruedas(4)
myCoche.cuanta_velocidad(200)
myCoche.asignar_cilindrada(40)

print("Las propiedades de myCoche son: ", vars(myCoche))

