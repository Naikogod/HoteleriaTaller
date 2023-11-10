# dao.py
import mysql.connector
from credenciales import DB_CONFIG

class DAO:
    def __init__(self):
        self.db = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.db.cursor()

    def verificar_credenciales(self, correo, contraseña):
        query = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
        self.cursor.execute(query, (correo, contraseña))

        # Obtener y leer el resultado
        result = self.cursor.fetchone()

        # Devolver el resultado
        return result

    def registrar_usuario(self, correo, contraseña):
        query = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"
        self.cursor.execute(query, (correo, contraseña))
        self.db.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.db.close()
    
    def registrar_cabana(self, numero_cabana, piesas, precio, estado):
        try:
            query = "INSERT INTO Cabanas (numero_cabana, piesas, precio, estado) VALUES (%s, %s, %s, %s)"
            values = (numero_cabana, piesas, precio, estado)
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error al registrar cabaña: {e}")
            return False

    def obtener_cabanas(self):
        query = "SELECT * FROM Cabanas"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def actualizar_cabana(self, numero_cabana, piesas, precio, estado):
        try:
            query = "UPDATE Cabanas SET piesas=%s, precio=%s, estado=%s WHERE numero_cabana=%s"
            values = (piesas, precio, estado, numero_cabana)
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cabaña: {e}")
            return False

