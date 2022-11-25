def main():

# crear clase vehiculo
    class vehiculo:
        def __init__(self, marca, modelo) -> None:
            self.marca = marca
            self.modelo = modelo

# instanciar clase vehiculo
    auto = vehiculo("Mazda",2010)
    texto = str(auto)

# guardarla en un archivo
    def escribir(text):
        f = open("vehiculo.txt","w")
        f.write(text)
        f.close

# y cargarla
    def leer(archivo):
        r = open(archivo,"r")
        text = r.read()
        r.close
        return text

    escribir(texto)
    a_imprimir = leer("vehiculo.txt")
    print(a_imprimir)

if __name__ == "__main__":
    main()