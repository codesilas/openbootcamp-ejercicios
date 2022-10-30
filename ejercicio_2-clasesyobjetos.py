# 1: crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.
# 2: Deberéis de definir los métodos para inicializar sus atributos
# 3. Deberás imprimirlos (sus atributos) y mostrar un mensaje con el resultado de la nota y si ha aprobado o no

class alumno():
    nombre:str = None
    Nota:int = None

    def asignar_nombre(self, a):
        self.nombre = a
        return self.nombre

    def asignar_nota(self, b):
        self.nota = b
        return self.nota
    
alumno_1 = alumno()
alumno_1.asignar_nombre("Juan")
alumno_1.asignar_nota(75)

alumno_2 = alumno()
alumno_2.asignar_nombre("Pedro")
alumno_2.asignar_nota(65)

def calificacion(alumno):
    if alumno.nota > 69:
        print(alumno.nombre,": aprobado.")
    else:
        print(alumno.nombre,": reprobado.")

calificacion(alumno_1)
calificacion(alumno_2)