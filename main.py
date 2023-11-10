# main.py
from dao import DAO
from login import LoginApp
from Admin import AdminApp

# Crear una instancia de la clase DAO (reemplaza esto con tu implementación real)
dao = DAO()

# Crear una instancia de la aplicación de inicio de sesión
login_app = LoginApp(dao)

# Cerrar la conexión al salir de la aplicación
def cerrar_aplicacion():
    dao.cerrar_conexion()
    login_app.root.destroy()

# Configurar la acción al cerrar la ventana principal
login_app.root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

# Iniciar el bucle principal de la aplicación de inicio de sesión
login_app.run()

# Verificar si el inicio de sesión fue exitoso antes de abrir la ventana de administración
if login_app.inicio_sesion_exitoso():
    # Crear una instancia de la aplicación de administración
    admin_app = AdminApp(dao, None)  # Asumiendo que no es necesario pasar una referencia de la ventana principal
    admin_app.run()
else:
    print("Inicio de sesión no exitoso. La aplicación no continuará.")
