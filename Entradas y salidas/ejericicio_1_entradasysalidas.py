def main():

    def escribir_archivo():
        f = open("archivo_prueba.txt", "w")
        f.write("Hola! este es un nuevo fichero de texto")
        f.close()

    def agregar_texto(texto):
        f = open("archivo_prueba.txt", "a")
        f.write(texto)
        f.close()

    escribir_archivo()
    agregar_texto("Este es un nuevo texto")

if __name__ == "__main__":
    main()