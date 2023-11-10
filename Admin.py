from tkinter import *
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from dao import DAO

class AdminApp:
    def __init__(self, dao, root):
        self.dao = dao
        self.root = ThemedTk(theme="arc")
        self.root.title("Administración de Cabañas")
        self.root.resizable(False, False)

        # Establecer el tamaño deseado para la ventana de administración
        window_width = 800
        window_height = 600
        self.root.geometry(f"{window_width}x{window_height}")

        self.frame_menu = Frame(self.root)
        self.frame_menu.pack(pady=10, padx=10)

        elementos_menu = [
            ("Registrar Cabaña", ttk.Button(self.frame_menu, text="Registrar Cabaña", command=self.mostrar_ventana_registro, style="TButton")),
            ("Mostrar Cabañas", ttk.Button(self.frame_menu, text="Mostrar Cabañas", command=self.mostrar_cabanas, style="TButton")),
            ("Actualizar Cabaña", ttk.Button(self.frame_menu, text="Actualizar Cabaña", command=self.actualizar_cabana, style="TButton"))
        ]

        for i, (texto, widget) in enumerate(elementos_menu):
            widget.grid(row=i, column=0, pady=5, padx=10, sticky="w")

        self.campos_registro = [
            ("Número de Cabaña", Entry(self.root)),
            ("Número de Piesas", Entry(self.root)),
            ("Precio", Entry(self.root)),
            ("Estado", ttk.Combobox(self.root, values=["Ocupada", "No Ocupada"]))
        ]

        self.btn_realizar_registro = ttk.Button(self.root, text="Realizar Registro", command=self.registrar_cabana, style="TButton")

    def mostrar_ventana_registro(self):
        ventana_registro = Toplevel(self.root)
        ventana_registro.title("Registro de Cabaña")

        frame_registro = Frame(ventana_registro)
        frame_registro.pack(pady=10, padx=10)

        for i, (texto, widget) in enumerate(self.campos_registro):
            label = Label(frame_registro, text=texto)
            label.pack(pady=5, padx=10, anchor="w")

            if texto == "Estado":
                combobox = ttk.Combobox(frame_registro, values=["Ocupada", "No Ocupada"])
                combobox.pack(pady=5, padx=10, fill='x')
                self.campos_registro[i] = (texto, combobox)
            else:
                entry = Entry(frame_registro)
                entry.pack(pady=5, padx=10, fill='x')
                self.campos_registro[i] = (texto, entry)

        btn_registrar = ttk.Button(frame_registro, text="Registrar", command=lambda: self.registrar_cabana_ventana(self.campos_registro, ventana_registro))
        btn_registrar.pack(pady=10, padx=10)

    def registrar_cabana_ventana(self, campos_cabana, ventana_registro):
        numero_cabana = campos_cabana[0][1].get()
        piesas = campos_cabana[1][1].get()
        precio = campos_cabana[2][1].get()
        estado = campos_cabana[3][1].get()

        if not numero_cabana or not piesas or not precio or not estado:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        if self.dao.registrar_cabana(numero_cabana, piesas, precio, estado):
            messagebox.showinfo("Éxito", "Cabaña registrada exitosamente.")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "Error al registrar la cabaña.")

    def registrar_cabana(self):
        ventana_registro = Toplevel(self.root)
        ventana_registro.title("Registro de Cabaña")

        frame_registro = Frame(ventana_registro)
        frame_registro.pack(pady=10, padx=10)

        campos_cabana = [
            ("Número de Cabaña", Entry(frame_registro)),
            ("Número de Piesas", Entry(frame_registro)),
            ("Precio", Entry(frame_registro)),
            ("Estado", ttk.Combobox(frame_registro, values=["Ocupada", "No Ocupada"]))
        ]

        for i, (texto, widget) in enumerate(campos_cabana):
            label = Label(frame_registro, text=texto)
            label.grid(row=i, column=0, pady=5, padx=10, sticky="w")
            widget.grid(row=i, column=1, pady=5, padx=10, sticky="w")

        btn_registrar = ttk.Button(frame_registro, text="Registrar", command=lambda: self.registrar_cabana_ventana(campos_cabana, ventana_registro), style="TButton")
        btn_registrar.grid(row=len(campos_cabana), column=0, pady=5, padx=10, sticky="w")

    def registrar_cabana_ventana(self, campos_cabana, ventana_registro):
        numero_cabana = campos_cabana[0][1].get()
        piesas = campos_cabana[1][1].get()
        precio = campos_cabana[2][1].get()
        estado = campos_cabana[3][1].get()

        if not numero_cabana or not piesas or not precio or not estado:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        if self.dao.registrar_cabana(numero_cabana, piesas, precio, estado):
            messagebox.showinfo("Éxito", "Cabaña registrada exitosamente.")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "Error al registrar la cabaña.")

    def mostrar_cabanas(self):
        cabanas = self.dao.obtener_cabanas()

        detalle_window = Toplevel(self.root)
        detalle_window.title("Detalles de Cabañas")

        window_width = 400
        window_height = 300
        x_position = (self.root.winfo_screenwidth() - window_width) // 2
        y_position = (self.root.winfo_screenheight() - window_height) // 2

        detalle_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        frame_detalle = Frame(detalle_window)
        frame_detalle.pack(pady=10, padx=10)

        for i, cabana in enumerate(cabanas):
            mensaje = f"Número de Cabaña: {cabana[0]}, Piesas: {cabana[1]}, Precio: {cabana[2]}, Estado: {cabana[3]}"
            label = Label(frame_detalle, text=mensaje)
            label.grid(row=i, column=0, pady=5, padx=10, sticky="w")

    def actualizar_cabana(self):
        cabanas = self.dao.obtener_cabanas()

        actualizar_window = Toplevel(self.root)
        actualizar_window.title("Actualizar Cabaña")

        window_width = 400
        window_height = 300
        x_position = (self.root.winfo_screenwidth() - window_width) // 2
        y_position = (self.root.winfo_screenheight() - window_height) // 2

        actualizar_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        frame_actualizar = Frame(actualizar_window)
        frame_actualizar.pack(pady=10, padx=10)

        label_seleccionar = Label(frame_actualizar, text="Seleccionar Cabaña:")
        label_seleccionar.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        combo_cabanas = ttk.Combobox(frame_actualizar, values=[str(cabana[0]) for cabana in cabanas])
        combo_cabanas.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        btn_mostrar = ttk.Button(frame_actualizar, text="Mostrar Detalles", command=lambda: self.mostrar_detalle_cabana(cabanas, combo_cabanas.get(), actualizar_window))
        btn_mostrar.grid(row=1, column=0, pady=5, padx=10, sticky="w")

    def mostrar_detalle_cabana(self, cabanas, numero_cabana, ventana_padre):
        cabaña_seleccionada = next((cabana for cabana in cabanas if str(cabana[0]) == numero_cabana), None)

        if cabaña_seleccionada:
            detalle_cabana_window = Toplevel(ventana_padre)
            detalle_cabana_window.title(f"Detalles de Cabaña {numero_cabana}")

            frame_detalle_cabana = Frame(detalle_cabana_window)
            frame_detalle_cabana.pack(pady=10, padx=10)

            mensaje = f"Número de Cabaña: {cabaña_seleccionada[0]}, Piesas: {cabaña_seleccionada[1]}, Precio: {cabaña_seleccionada[2]}, Estado: {cabaña_seleccionada[3]}"
            label = Label(frame_detalle_cabana, text=mensaje)
            label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

            campos_editables = [
                ("Número de Piesas:", Entry(frame_detalle_cabana)),
                ("Precio:", Entry(frame_detalle_cabana)),
                ("Estado:", ttk.Combobox(frame_detalle_cabana, values=["Ocupada", "No Ocupada"]))
            ]

            for i, (texto, widget) in enumerate(campos_editables):
                label = Label(frame_detalle_cabana, text=texto)
                label.grid(row=i + 1, column=0, pady=5, padx=10, sticky="w")
                widget.grid(row=i + 1, column=1, pady=5, padx=10, sticky="w")

            btn_actualizar = ttk.Button(frame_detalle_cabana, text="Actualizar Cabaña",
                                        command=lambda: self.actualizar_cabana_detalle(numero_cabana, campos_editables))
            btn_actualizar.grid(row=len(campos_editables) + 1, column=0, pady=5, padx=10, sticky="w")

        else:
            messagebox.showerror("Error", f"No se encontró la cabaña con el número {numero_cabana}.")

    def actualizar_cabana_detalle(self, numero_cabana, campos_editables):
        nuevos_datos = [widget.get() if isinstance(widget, Entry) else widget.get() for _, widget in campos_editables]

        if not all(nuevos_datos):
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        if self.dao.actualizar_cabana(numero_cabana, *nuevos_datos):
            messagebox.showinfo("Éxito", "Información de la cabaña actualizada exitosamente.")
        else:
            messagebox.showerror("Error", "Error al actualizar la información de la cabaña.")

    def run(self):
        self.root.mainloop()

# Código para correr la aplicación si se ejecuta este script directamente
if __name__ == "__main__":
    dao = DAO()  # Debes crear una instancia de DAO aquí con tu implementación real
    admin_app = AdminApp(dao, None)
    admin_app.run()
