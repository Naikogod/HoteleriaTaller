# login.py
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from validate_email_address import validate_email
from tkinter import messagebox
from Admin import AdminApp

class LoginApp:
    def __init__(self, dao):
        self.dao = dao

        # Crear la ventana principal con ThemedTk
        self.root = ThemedTk(theme="arc")
        self.root.title("Inicio de Sesión")
        self.root.resizable(False, False)

        # Crear la variable después de la creación de la ventana principal
        self.inicio_sesion_exitoso_var = BooleanVar(value=False)

        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Definir dimensiones y posición de la ventana
        window_width = 400
        window_height = 300
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Crear y colocar los widgets en la ventana
        frame_principal = Frame(self.root)
        frame_principal.pack(pady=10, padx=10, anchor="w")

        elementos = [
            ("Correo:", Entry(frame_principal)),
            ("Contraseña:", Entry(frame_principal, show="*")),
            ("Mostrar Contraseña", ttk.Checkbutton(frame_principal, command=self.toggle_password)),
            ("Iniciar Sesión", ttk.Button(frame_principal, text="Iniciar Sesión", command=self.login, style="TButton")),
            ("Registrarse", ttk.Button(frame_principal, text="Registrarse", command=self.registrar, style="TButton"))
        ]

        for i, (texto, widget) in enumerate(elementos):
            label = Label(frame_principal, text=texto)
            label.grid(row=i, column=0, pady=5, padx=10, sticky="w")
            widget.grid(row=i, column=1, pady=5, padx=10, sticky="w")

        self.entry_correo = elementos[0][1]
        self.entry_contraseña = elementos[1][1]

    def login(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()

        if correo == "" or contraseña == "":
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
        elif not self.validar_correo(correo):
            messagebox.showerror("Error", "Correo electrónico no válido.")
        else:
            resultado = self.dao.verificar_credenciales(correo, contraseña)

            if resultado:
                self.inicio_sesion_exitoso_var.set(True)
                # Mostrar mensaje de inicio de sesión exitoso
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                # Cerrar la ventana de inicio de sesión
                self.root.destroy()
                # Abrir la ventana de administración
                self.iniciar_administracion()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")

    def inicio_sesion_exitoso(self):
        return self.inicio_sesion_exitoso_var.get()

    def registrar(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()

        if correo == "" or contraseña == "":
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
        elif not self.validar_correo(correo):
            messagebox.showerror("Error", "Correo electrónico no válido.")
        else:
            self.dao.registrar_usuario(correo, contraseña)
            messagebox.showinfo("Éxito", "Registro exitoso.")

    def validar_correo(self, correo):
        if not validate_email(correo, verify=False):
            return False

        if ".com" not in correo:
            return False

        return True

    def toggle_password(self):
        current_state = self.entry_contraseña["show"]
        new_state = "" if current_state else "*"
        self.entry_contraseña["show"] = new_state

    def run(self):
        self.root.mainloop()

    def iniciar_administracion(self):
        admin_app = AdminApp(self.dao, self.root)
        admin_app.run()
        self.root.destroy()
