import sqlite3
import sys 

try: 
    databaseName= "diccionarioCh.db" 
    
    def obtener_conexion(): 
        return sqlite3.connect(databaseName)

    def crearTablas():
        tablas = [ " CREATE TABLE IF NOT EXISTS diccionario( id INTEGER PRIMARY KEY AUTOINCREMENT, palabra TEXT NOT NULL, significado TEXT NOT NULL)"]
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        for tabla in tablas:
            cursor.execute(tabla)
        
        
    def principal():
        crearTablas()
        menu = """
    \n-------------------------------------------
            DICCIONARIO DE SLANG PANAMEÑO
    a) Agregar nueva palabra:
    b) Editar palabra existente:
    c) Eliminar palabra existente:
    d) Ver listado de palabras:
    e) Buscar significado de palabra:
    f) Salir
    -------------------------------------------
    Selecciona una opción: """

        option = ""
        while option != "f":
            option = input(menu)
            if option == "a": 
                palabra = input("Ingrese la palabra: ")
                significadoPosible = obtener_significado(palabra)
                if significadoPosible: 
                    print(f"La palabra '{palabra}' ya existe")
                else:
                    significado = input("Ingrese el significado: ")
                    addPalabra (palabra, significado)
                    print(f"Palabra agregada: {palabra}")
            if option == "b":
                palabra = input("Ingresa la palabra que quieres editar: ")
                nuevoSignificado = input("Ingresa el nuevo significado: ")
                editPalabra (palabra, nuevoSignificado)
                print(f"Palabra actualizada: {palabra}")
            if option == "c":
                palabra = input("Ingresa la palabra a eliminar: ")
                removePalabra(palabra)
                print(f"Palabra eliminada: {palabra}")
            if option == "d":
                palabras  = obtenerPalabra()
                print("=== Lista de palabras ===")
                for palabra in palabras:
                    print(palabra[0])
            if option == "e":
                palabra = input("Ingresa la palabra de la cual quieres saber el significado: ")
                significado = obtener_significado(palabra)
                if significado:
                    print(f"El significado de '{palabra}' es: {significado[0]}")
                else:
                    print(f"Palabra '{palabra}' no encontrada")
        else: 
            print("\nEl programa ha finalizado, bye...")
            sys.exit()


    #METODOS

    def addPalabra(palabra, significado):
        conexion  = obtener_conexion()
        cursor = conexion.cursor()
        declarar = "INSERT INTO diccionario (palabra, significado) VALUES (?, ?)"
        cursor.execute(declarar, [palabra, significado])
        conexion.commit()


    def obtener_significado(palabra):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        declarar = "SELECT significado FROM diccionario WHERE palabra = ?"
        cursor.execute(declarar, [palabra])
        return cursor.fetchone()
    
    def editPalabra(palabra, nuevoSignificado):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        declarar = "UPDATE diccionario SET significado = ? WHERE palabra = ?"
        cursor.execute(declarar, [nuevoSignificado , palabra])
        conexion.commit()

    def removePalabra(palabra):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        declarar = "DELETE FROM diccionario WHERE palabra = ?"
        cursor.execute(declarar, [palabra])
        conexion.commit()

    def obtenerPalabra():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        declarar = "SELECT palabra FROM diccionario"
        cursor.execute(declarar)
        return cursor.fetchall()


    if __name__ == '__main__':
        principal() 


finally:
    conexion = obtener_conexion()
    obtener_conexion().close
        