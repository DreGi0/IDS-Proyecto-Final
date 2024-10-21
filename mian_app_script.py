from tkinter import *
from tkinter import ttk
import pandas as pd
import json

class MainApp:
    def __init__(self, root):
        self.load_student_data()
        self.setup_ui(root)
        
        self.student_id = StringVar()
        self.manager_pass = StringVar()

        self.setup_role_selection()

    # ==================== DATA LOADING ====================
    def load_student_data(self):
        try:
            self.student_table = pd.read_excel("Data/dta_student_id.xlsx", sheet_name="Student_IDs")
        except Exception as e:
            print(f"Error loading the file: {e}")

    # ==================== UI SETUP ====================
    def setup_ui(self, root):
        root.title("Prototype - 0.1.0")
        root.geometry("500x200")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    # ==================== ROLE SELECTION ====================
    def setup_role_selection(self):
        self.role = StringVar()
        role_options = ["Estudiante", "Administrador"]
        
        ttk.Label(self.mainframe, text="Seleccione rol:").grid(column=1, row=1)
        self.role_combobox = ttk.Combobox(self.mainframe, textvariable=self.role, values=role_options, state='readonly')
        self.role_combobox.grid(column=2, row=1, sticky="W, E")
        self.role_combobox.current(0)
        self.role_combobox.bind("<<ComboboxSelected>>", self.setup_login_fields)
        
        self.setup_login_fields()

    # ==================== LOGIN FIELDS ====================
    def setup_login_fields(self, event=None):
        self.clear_mainframe()
        ttk.Label(self.mainframe, text="Seleccione rol:").grid(column=1, row=1)
        self.role_combobox.grid(column=2, row=1, sticky="W, E")

        if self.role.get() == "Estudiante":
            self.create_login_field("Ingrese número de carnet:", self.student_id, self.handle_login)
        else:
            self.create_login_field("Ingrese contraseña de administrador:", self.manager_pass, self.handle_login, show='*')

    def create_login_field(self, label_text, var, command, show=''):
        ttk.Label(self.mainframe, text=label_text).grid(column=1, row=2)
        entry = ttk.Entry(self.mainframe, width=15, textvariable=var, show=show)
        entry.grid(column=2, row=2, sticky="W, E")
        entry.bind("<Return>", lambda event: command())
        ttk.Button(self.mainframe, text="Submit", command=command).grid(column=1, row=3, columnspan=2)
        entry.focus()

    # ==================== LOGIN HANDLING ====================
    def handle_login(self):
        role_validators = {"Estudiante": self.validate_student, "Administrador": self.validate_admin}
        selected_role = self.role.get()
        validator = role_validators.get(selected_role)
        if validator:
            input_value = self.student_id.get() if selected_role == "Estudiante" else self.manager_pass.get()
            validator(input_value)

    def validate_student(self, student_id_value):
        try:
            student_id_value = int(student_id_value)
            if student_id_value in self.student_table["Student ID"].values:
                name = self.student_table.loc[self.student_table["Student ID"] == student_id_value, "Name"].values[0]
                self.show_main_menu(name)
            else:
                self.show_error_message("ID no encontrado.")
        except ValueError:
            self.show_error_message("Por favor ingrese un ID válido.")
        except Exception as e:
            self.show_error_message(f"Error: {e}")

    def validate_admin(self, password):
        if password == '123':
            self.admin_menu_management()
        else:
            self.show_error_message("Contraseña incorrecta")

    # ==================== MAIN MENUS ====================
    def show_main_menu(self, student_name):
        self.clear_mainframe()
        ttk.Label(self.mainframe, text=f"Bienvenido, {student_name}!").grid(row=0, column=0, columnspan=3)
        self.create_menu_buttons([("Plato Fuerte", self.show_strong_plate_menu),
                                  ("Bebida", self.select_bebida),
                                  ("Acompañamiento", self.select_acompanamiento)])

    def admin_menu_management(self):
        self.clear_mainframe()
        ttk.Label(self.mainframe, text="Menú de Administración").grid(row=0, column=0, columnspan=2)
        self.create_menu_buttons([("Ver Reportes", self.view_reports), ("Gestionar Usuarios", self.manage_users)])

    def create_menu_buttons(self, options):
        for i, (label, command) in enumerate(options):
            ttk.Button(self.mainframe, text=label, command=command).grid(row=1, column=i, padx=10, pady=10)
        ttk.Button(self.mainframe, text="Volver al inicio", command=self.setup_role_selection).grid(row=2, column=0, columnspan=len(options))

    def show_strong_plate_menu(self):
        self.clear_mainframe()
        ttk.Label(self.mainframe, text="Seleccione el plato principal:").grid(row=0, column=0, columnspan=2)
        self.create_menu_buttons([("Pollo", lambda: self.select_option("Pollo")), 
                                  ("Carne", lambda: self.select_option("Carne"))])

    # ==================== UTILITY FUNCTIONS ====================
    def clear_mainframe(self):
        for widget in self.mainframe.winfo_children():
            widget.grid_forget()

    def show_error_message(self, message):
        self.clear_error_message()
        error_label = ttk.Label(self.mainframe, text=message, foreground="red")
        error_label.grid(column=1, row=4, columnspan=2)
        self.error_message_widget = error_label

    def clear_error_message(self):
        if hasattr(self, 'error_message_widget') and self.error_message_widget.winfo_ismapped():
            self.error_message_widget.grid_forget()

    def select_option(self, option):
        print(f"{option} seleccionado!")

    def select_bebida(self):
        print("Bebida seleccionada!")

    def select_acompanamiento(self):
        print("Acompañamiento seleccionado!")

    def view_reports(self):
        print("Viendo reportes...")

    def manage_users(self):
        print("Gestionando usuarios...")

# ==================== RUN APP ====================
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
