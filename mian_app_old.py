from tkinter import *
from tkinter import ttk

import bcrypt

from scripts.data_processing import *
from scripts.stat_calculations import *
from utils.helpers import *

"""
Version  0.2.1 - prototype
Comment definition
# ==================== NAME ==================== : usado para titular secciones de la aplicación o conetenedores principales

# -------------------- NAME -------------------- : usado para titular funciones dentro de los contenedores

# ----- name ----- : usado para titular secciones dentro de las funciones

# description : usado para dar descripciones de la funcionalidad

## comentario : usado para destacar puntos importantes a tomar en cuenta
"""

class MainApp:
    def __init__(self, root):

        self.student_table = load_student_data("data/students_data.xlsx")
        self.setup_app(root)
    
        # ----- Variables para campos de entrada -----
        self.student_id = StringVar()
        self.manager_pass = StringVar()

        # ----- Iniciar widget de login -----
        self.login_widget()

    # ==================== CONFIGURACIÓN PRINCIPAL DE LA APP ====================
    def setup_app(self, root):
        # ----- Propiedades de la ventana -----
        root.title("CafeteriaGo version 0.2.1 - prototype")
        root.geometry("500x200")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")

        # ----- Grilla principal -----
        self.mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    
    # ==================== CONTENEDOR DE LA VENTANA LOGIN ====================
    def login_widget(self):
        self.setup_role_selection()

    # -------------------- SELECCION DE ROL --------------------
    def setup_role_selection(self):
        # ----- Variables -----
        self.role = StringVar()
        ROLE_OPTIONS = ["Estudiante", "Administrador"]
        
        # ----- Etiqueta y caja de slección de rol -----
        ttk.Label(self.mainframe, text="Seleccione rol:").grid(column=1, row=1) # texto intructivo
        self.role_combobox = ttk.Combobox(self.mainframe, textvariable=self.role, values=ROLE_OPTIONS, state='readonly') # Configuracion de la caja de opciones
        self.role_combobox.grid(column=2, row=1, sticky="W, E") 
        self.role_combobox.current(0) # Rol de estudiante por defecto
        self.role_combobox.bind("<<ComboboxSelected>>", self.setup_login_fields)

        # ----- Inicializar campos de login -----
        self.setup_login_fields()

    # -------------------- ESPACIOS DE TEXTO LOGIN --------------------
    def setup_login_fields(self, event=None):
        self.clear_mainframe()

        # ----- Restaurar la slección de rol -----
        ttk.Label(self.mainframe, text="Seleccione rol:").grid(column=1, row=1)
        self.role_combobox.grid(column=2, row=1, sticky="W, E")

        # ----- Mostrar campos de entrada dependiendo del rol seleccionado -----
        if self.role.get() == "Estudiante":
            self.create_login_field("Ingrese número de carnet:", self.student_id, self.process_login_action)
        else:
            self.create_login_field("Ingrese contraseña de administrador:", self.manager_pass, self.process_login_action, show='*')

    def create_login_field(self, label_text, var, command, show=''):
        ttk.Label(self.mainframe, text=label_text).grid(column=1, row=2)
        entry = ttk.Entry(self.mainframe, width=15, textvariable=var, show=show)
        entry.grid(column=2, row=2, sticky="W, E")
        entry.bind("<Return>", lambda event: command()) # Liga el comando con la tecla Return (Enter)
        ttk.Button(self.mainframe, text="Submit", command=command).grid(column=1, row=3, columnspan=2)
        entry.focus() # Cuando es creado se selecciona

    # -------------------- MANEJO DE LOGIN --------------------
    def process_login_action(self):
        role_validators = {
            "Estudiante": self.validate_student, 
            "Administrador": self.validate_admin
        }
        
        selected_role = self.role.get()
        validator = role_validators.get(selected_role)

        if validator:
            input_value = self.student_id.get() if selected_role == "Estudiante" else self.manager_pass.get()
            validator(input_value)
    
    # -------------------- VALIDACIÓN DE ESTUDIANTE --------------------
    def validate_student(self, student_id_value): # Valida si existe el id del estudiante y si se presenta un error lo muestra en pantalla
        try:
            student_id_value = int(student_id_value)
            if student_id_value in self.student_table["Student ID"].values:
                self.student_name = self.student_table.loc[self.student_table["Student ID"] == student_id_value, "Name"].values[0]
                self.display_main_menu_for_student()
            else:
                self.show_error_message("ID no encontrado.")
        except ValueError:
            self.show_error_message("Por favor ingrese un ID válido.")
        except Exception as e:
            self.show_error_message(f"Error: {e}")

    # -------------------- VALIDACIÓN DE ADMINISTRADOR --------------------
    def validate_admin(self, password):
        hashed_password = load_admin_password()

        if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            self.display_main_menu_for_admin()
        else:
            self.show_error_message("Contraseña incorrecta")
    
    # ==================== CONTENEDOR DE LA VENTANA DE ESTUDIANTE ====================
    def display_main_menu_for_student(self):  # Muestra el menú principal para el estudiante.
        self.clear_mainframe()

        # ----- Titulo de de bienvenida de la página -----
        welcome_text = ttk.Label(self.mainframe, text=f"Bienvenido, {self.student_name}!", anchor="center")

        # ----- Opciones de menú -----
        options = [
            ("Plato Fuerte", self.show_strong_plate_menu),
            ("Bebida", self.show_drink_menu),
            ("Acompañamiento", self.show_complement_menu),
            ("Ensalada", self.show_salad_menu)
        ]

        welcome_text.grid(row=0, column=0, columnspan=len(options), pady=10, sticky="EW")

        for i, (label, command) in enumerate(options):
            ttk.Button(self.mainframe, text=label, command=command).grid(row=1, column=i, padx=10, pady=10, sticky="E, W")

        ttk.Button(self.mainframe, text="Volver al inicio", command=self.setup_role_selection).grid(row=2, column=1, columnspan=2, pady=10, sticky="E, W")

    # ==================== VENTANAS DE OPCIONES DE MENÚ ====================
    def show_strong_plate_menu (self):
        self.show_menu("Selecione el plato principal", [
            ("Pollo", lambda: self.select_option("Pollo")), 
            ("Carne", lambda: self.select_option("Carne")),
            ("Sandwich", lambda: self.select_option("Sandwich"))
        ])

    def show_drink_menu (self):
        self.show_menu("Selecione el plato principal", [
            ("Coke", lambda: self.select_option("Coke")), 
            ("Fanta", lambda: self.select_option("Fanta"))
        ])
    
    def show_complement_menu (self):
        self.show_menu("Selecione el plato principal", [
            ("Arroz", lambda: self.select_option("Arroz")), 
            ("Casamiento", lambda: self.select_option("Casamiento")),
        ])
    
    def show_salad_menu (self):
        self.show_menu("Selecione el plato principal", [
            ("Ensalada fresca", lambda: self.select_option("Ensalada fresca")), 
            ("Coditos", lambda: self.select_option("Coditos"))
        ])

    def show_menu(self, label, options):
        self.clear_mainframe()
        ttk.Label(self.mainframe, text=label).grid(row=0, column=0, columnspan=3)
        self.create_menu_buttons(options)
        ttk.Button(self.mainframe, text="Volver atras", command=self.display_main_menu_for_student).grid(row=3, column=0, columnspan=3)

    def select_option (self, option):
        print(f"{option} selected!")

    # ==================== CONTENEDOR DE LA VENTANA DE AMINISTRADOR ====================
    def display_main_menu_for_admin(self):
        self.clear_mainframe()
        ttk.Label(self.mainframe, text="Menú de Administración").grid(row=0, column=0, columnspan=2)
        self.create_menu_buttons([("Ver Reportes", self.view_reports), ("Gestionar Usuarios", self.manage_users), ("Cambiar contraseña", self.change_admin_password)])
        ttk.Button(self.mainframe, text="Volver al inicio", command=self.setup_role_selection).grid(row=2, column=0, columnspan=3)

    # -------------------- OPCIONES DE AMINISTRADOR --------------------
    def create_menu_buttons(self, options): # Crea los botones con las opcion dadas
        for i, (label, command) in enumerate(options):
            ttk.Button(self.mainframe, text=label, command=command).grid(row=1, column=i, padx=10, pady=10)

    def change_admin_password(self):
        self.clear_mainframe()

        ttk.Label(self.mainframe, text="La contraseña debe conter algún digno").grid(column=0, row=0)
        ttk.Label(self.mainframe, text="La contraseña debe conter algún digno").grid(column=9, row=0)
        ttk.Label(self.mainframe, text="La contraseña debe conter algún digno")

        old_password_row = 2
        self.test("Ingrese la contraseña actual: ", old_password_row)

        old_password_var = StringVar()
        old_password_entry = ttk.Entry(self.mainframe, textvariable=old_password_var, show='*')
        old_password_entry.grid(column=2, row=old_password_row)

        new_password_row = 3
        self.test("Ingrese nueva contraseña: ", new_password_row)
        new_password_var = StringVar()
        new_password_entry = ttk.Entry(self.mainframe, textvariable=new_password_var, show='*')
        new_password_entry.grid(column=2, row=2)

        ttk.Button(self.mainframe, text="Guardar", command=lambda: self.check_old_password(old_password_var.get(), new_password_var.get())).grid(column=1, row=3, columnspan=2)
        ttk.Button(self.mainframe, text="Volver atras", command=self.display_main_menu_for_admin).grid(row=5, column=0, columnspan=3, pady=10, sticky="E, W")

    def test(self, label, row):
        ttk.Label(self.mainframe, text=label).grid(column=1, row=row)


    def check_old_password(self, password, new_password):
        hashed_password = load_admin_password()

        if hashed_password and not compare_password(password):
            self.show_error_message("Contraseña incorrecta")
        elif hashed_password and compare_password(new_password):
            self.show_error_message("La contraseña no puede sar la msima que la actual")
        elif not new_password or len(new_password) > 10:
            self.show_error_message("Agregue una contraseña valida")
        else:
            print(f"Password changed to: {new_password}")
            self.save_new_password(new_password)

    def save_new_password(self, new_password):
        save_admin_password(new_password)  # Llama a la función que guarda la nueva contraseña
        self.show_error_message("Contraseña actualizada con éxito.", "green")



    #--
    def clear_mainframe(self): # Limpia la grilla completa de la ventana actual (borra todo en pantalla)
        for widget in self.mainframe.winfo_children():
            widget.grid_forget()

    def show_error_message(self, message, color="red"): # Muestra un texto en pantalla con rojo por defecto
        self.clear_error_message()
        error_label = ttk.Label(self.mainframe, text=message, foreground=color)
        error_label.grid(column=1, row=4, columnspan=2)
        self.error_message_widget = error_label

    def clear_error_message(self): # Limpia el texto en rojo en pantalla
        if hasattr(self, 'error_message_widget') and self.error_message_widget.winfo_ismapped():
            self.error_message_widget.grid_forget()
    def view_reports(self):
        print("Viendo reportes...")

    def manage_users(self):
        print("Gestionando usuarios...")




if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()