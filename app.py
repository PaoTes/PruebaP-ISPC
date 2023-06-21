import sqlite3

def conectar():
    conexion = sqlite3.connect("myBD.db")
    cursor = conexion.cursor()
    return conexion, cursor
    #crear la conexion para la base de datos

def crearTabla():
    conexion, cursor = conectar()
    sql = """     

        CREATE TABLE IF NOT EXISTS leyes(
            n_registro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            n_normativa VARCHAR(10) NOT NULL,
            fecha DATE NOT NULL,
            descripcion VARCHAR(300) NOT NULL,
            o_legislativo VARCHAR(50)NOT NULL,
            p_clave VARCHAR(50) NOT NULL,
            FOREIGN KEY (tnormativa_id) REFERENCES tnormativa(id),
            FOREIGN KEY (categoria_id) REFERENCES categoria(id),
            FOREIGN KEY (jurisdiccion_id) REFERENCES jurisdiccion(id)
        );
        
        CREATE TABLE IF NOT EXISTS tnormativa(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(50) NOT NULL
        );
        

        CREATE TABLE IF NOT EXISTS categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(50) NOT NULL
        );
    

        CREATE TABLE IF NOT EXISTS jurisdiccion(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(50) NOT NULL
         );
    """
    if (cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()

crearTabla()
    
