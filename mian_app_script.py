from tkinter import *
from tkinter import ttk
import pandas as pd
import json

class MainApp:
    # ==================== MAIN APP ====================
    def __init__(self, root):  # Inicializa la aplicación y carga los datos de estudiantes.
        self.load_student_data()
        self.setup_ui(root)
        
        self.student_id = StringVar()
        self.manager_pass = StringVar()

        self.setup_role_selection()

    # ==================== DATA LOADING ====================
    def load_student_data(self):  # Carga los datos de estudiantes desde un archivo Excel.
        try:
            self.student_table = pd.read_excel("IDS-Proyecto-Final/Data/dta_student_id.xlsx", sheet_name="Student_IDs")
        except Exception as e:
            print(f"Error loading the file: {e}")

    # ==================== UI SETUP ====================
    def setup_ui(self, root):  # Configura la interfaz de usuario principal.
        root.title("Prototype - 0.1.0")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky="N, W, E, S")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    # ==================== ROLE SELECTION ====================
    def setup_role_selection(self):  # Configura la selección del rol (Estudiante/Administrador).
        self.role = StringVar()
        ttk.Label(self.mainframe, text="Seleccione rol:").grid(column=1, row=1)

        role_options = ["Estudiante", "Administrador"]
        self.role_combobox = ttk.Combobox(self.mainframe, textvariable=self.role, values=role_options, state='readonly')
        self.role_combobox.grid(column=2, row=1, sticky="W, E")
        self.role_combobox.current(0)
        self.role_combobox.bind("<<ComboboxSelected>>", self.update_login_fields)

        self.setup_login_fields()

    # ==================== LOGIN FIELDS ====================
    def setup_login_fields(self):  # Configura los campos de inicio de sesión según el rol seleccionado.
        for widget in self.mainframe.winfo_children():
            widget.grid_forget()

        ttk.Label(self.mainframe, text="Seleccione rol:").grid(column=1, row=1)
        self.role_combobox.grid(column=2, row=1, sticky="W, E")

        if self.role.get() == "Estudiante":
            self.setup_student_login()
        else:
            self.setup_admin_login()

    def setup_student_login(self):  # Configura los campos de inicio de sesión para estudiantes.
        ttk.Label(self.mainframe, text="Ingrese número de carnet:").grid(column=1, row=2)
        student_id_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.student_id)
        student_id_entry.grid(column=2, row=2, sticky="W, E")
        ttk.Button(self.mainframe, text="Submit", command=self.handle_login).grid(column=1, row=3, columnspan=2)
        student_id_entry.focus()

    def setup_admin_login(self):  # Configura los campos de inicio de sesión para administradores.
        ttk.Label(self.mainframe, text="Ingrese contraseña de administrador:").grid(column=1, row=2)
        manager_pass_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.manager_pass, show='*')
        manager_pass_entry.grid(column=2, row=2, sticky="W, E")
        ttk.Button(self.mainframe, text="Submit", command=self.handle_login).grid(column=1, row=3, columnspan=2)
        manager_pass_entry.focus()

    # ==================== LOGIN HANDLING ====================
    def update_login_fields(self, event):  # Actualiza los campos de inicio de sesión según el rol seleccionado.
        self.setup_login_fields()

    def handle_login(self):  # Maneja el inicio de sesión basado en el rol seleccionado.
        role_validators = {
            "Estudiante": self.validate_student,
            "Administrador": self.validate_admin
        }
        selected_role = self.role.get()
        validator = role_validators.get(selected_role)
        if validator:
            validator(self.student_id.get() if selected_role == "Estudiante" else self.manager_pass.get())

    def validate_student(self, student_id_value):  # Valida el ID de estudiante y muestra el menú principal si es válido.
        try:
            student_id_value = int(student_id_value)
            if student_id_value in self.student_table["Student ID"].values:
                name = self.student_table.loc[self.student_table["Student ID"] == student_id_value, "Name"].values[0]
                self.show_main_menu(name)
            else:
                print("ID not found")
        except ValueError:
            print("Por favor ingrese un ID válido.")
        except Exception as e:
            print(f"Error: {e}")

    def validate_admin(self, password):  # Valida la contraseña del administrador y muestra el menú de administrador si es válida.
        if password == '123':
            print("Access granted for administrator.")
            self.admin_menu_management()
        else:
            print("Incorrect password.")

    # ==================== MAIN MENUS ====================
    def show_main_menu(self, student_name):  # Muestra el menú principal para el estudiante.
        self.clear_mainframe()
        ttk.Label(self.mainframe, text=f"Welcome, {student_name}!").grid(row=0, column=0, columnspan=3)
        self.create_menu_buttons()

    def create_menu_buttons(self):  # Crea botones para el menú principal.
        options = [("Plato Fuerte", self.show_strong_plate_menu),
                   ("Bebida", self.select_bebida),
                   ("Acompañamiento", self.select_acompanamiento)]
        for i, (label, command) in enumerate(options):
            ttk.Button(self.mainframe, text=label, command=command).grid(row=1, column=i, padx=10, pady=10)

        ttk.Button(self.mainframe, text="Back to Login", command=self.setup_role_selection).grid(row=2, column=0, columnspan=3)

    def admin_menu_management(self):  # Muestra el menú de administración.
        self.clear_mainframe()
        ttk.Label(self.mainframe, text="Admin Menu").grid(row=0, column=0, columnspan=2)
        admin_options = [("View Reports", self.view_reports), 
                         ("Manage Users", self.manage_users)]
        for i, (label, command) in enumerate(admin_options):
            ttk.Button(self.mainframe, text=label, command=command).grid(row=1, column=i, padx=10, pady=10)

        ttk.Button(self.mainframe, text="Back to Login", command=self.setup_role_selection).grid(row=2, column=0, columnspan=2)

    def show_strong_plate_menu(self):  # Muestra el menú de platos fuertes.
        self.clear_mainframe()
        ttk.Label(self.mainframe, text="Selecciona el plato principal:").grid(row=0, column=0, columnspan=2)
        plate_options = [("Chicken", lambda: self.select_option("Chicken")), 
                         ("Beef", lambda: self.select_option("Beef"))]
        for i, (label, command) in enumerate(plate_options):
            ttk.Button(self.mainframe, text=label, command=command).grid(row=1, column=i, padx=10, pady=10)

        ttk.Button(self.mainframe, text="Back", command=lambda: self.show_main_menu("")).grid(row=2, column=0, columnspan=2)

    # ==================== UTILITY FUNCTIONS ====================
    def clear_mainframe(self):  # Limpia el marco principal de widgets existentes.
        for widget in self.mainframe.winfo_children():
            widget.grid_forget()

    def select_option(self, option):  # Maneja la selección de una opción del menú.
        print(f"{option} selected!")

    def select_bebida(self):  # Maneja la selección de la opción bebida.
        print("Bebida selected!")

    def select_acompanamiento(self):  # Maneja la selección de la opción acompañamiento.
        print("Acompañamiento selected!")

    def view_reports(self):  # Maneja la visualización de reportes.
        print("Viewing reports...")

    def manage_users(self):  # Maneja la gestión de usuarios.
        print("Managing users...")

# ==================== RUN APP ====================
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
