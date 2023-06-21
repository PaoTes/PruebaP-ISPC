import sqlite3

def conectar():
    conexion = sqlite3.connect("myBD.db")
    cursor = conexion.cursor()
    return conexion, cursor
    #crear la conexion para la base de datos

def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLA IF NOT EXISTS leyes(
            n_registro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            n_normativa VARCHAR(10),
            fecha DATE,
            descripcion VARCHAR(300),
            o_legislativo VARCHAR(50),
            p_clave VARCHAR(50)
            FOREIGN KEY (tnormativa_id) REFERENCES tnormativa(id),
            FOREIGN KEY (categoria_id) REFERENCES categoria(id),
            FOREIGN KEY (jurisdiccion_id) REFERENCES jurisdiccion(id)
        )
    """
    
print ("hello world")