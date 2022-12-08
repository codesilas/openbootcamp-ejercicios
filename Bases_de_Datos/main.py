import sqlite3

def buscar_query(nombre):
    name = nombre
    conn = sqlite3.connect("prueba.db")
    cursor = conn.cursor()
    resultado = cursor.execute(f'SELECT * FROM Alumnos WHERE nombre="{name}"')
    return resultado

nombre = input("¿Qué nombre quieres buscar? :")

buscar = buscar_query(nombre)

for fila in buscar:
    print(fila)