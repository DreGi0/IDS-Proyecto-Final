from tkinter import *
from tkinter import ttk

from scripts.data_processing import *
from scripts.stat_calculations import *
from utils.helpers import *

"""
Comment definition
# ======================================== NAME ======================================== : usado para titular secciones de la aplicación o conetenedores principales

# ---------------------------------------- NAME ---------------------------------------- : usado para titular funciones dentro de los contenedores

# ----- name ----- : usado para titular secciones dentro de las funciones

# description : usado para dar descripciones de la funcionalidad

## comentario : usado para destacar puntos importantes a tomar en cuenta
"""

version = "0.3.0 - prototype"

class MainApp():
    # ======================================== INITIALIZE APP ========================================
    def __init__(self, root_window):

        # ----- Variables para campos de entrada -----
        self.student_table = load_student_data("data/students_data.xlsx")
        self.setup_app(root_window)

        self.setup_styles()

        # ----- Variables para campos de entrada -----
        self.student_id = StringVar()
        self.admin_user = StringVar()
        self.admin_pass = StringVar()

        # ----- Iniciar widget de login -----
        self.setup_login_frame()

    # ---------------------------------------- MAIN WINDOW CONFIGURATION ---------------------------------------- 
    def setup_app(self, root_window):
        # ----- Window properties -----
        root_window.title(f"CafeteriaGo version {version}")
        self.mainframe = ttk.Frame(root_window, padding="30 60 30 60")

        # ----- Main grid -----
        self.mainframe.grid(column=0, row=0)
        root_window.columnconfigure(0, weight=1)
        root_window.rowconfigure(0, weight=1)

    # ---------------------------------------- STYLES CONFIGURATION ---------------------------------------- 
    def setup_styles(self):
        self.style = ttk.Style()

        self.style.configure("BW.TLabel", background="grey80")
        self.style.configure("M.TLabel", background="red")

        self.style.configure("H1.TLabel", background="grey80", foreground="black", font=("Consolas", 16, "bold"))
        self.style.configure("H2.TLabel", background="grey80", foreground="black", font=("Consolas", 11))


        self.setup_styles_constants()
    
    def setup_styles_constants(self):
        self.HEADER1 = "H1.TLabel"
        self.HEADER2 = "H2.TLabel"

    # ======================================== LOGIN WINDOW ========================================
    def setup_login_frame(self):
        
        self.login_frame = ttk.Frame(self.mainframe, width=500, height=300, style="BW.TLabel")
        self.login_frame.grid(column=0, row=0)
        self.login_frame.grid_propagate(False)

        self.login_frame.columnconfigure(0, weight=1)
        self.login_frame.columnconfigure(1, weight=1)


        welcome_label = ttk.Label(self.login_frame, text="Bienvenido", style=self.HEADER1, anchor='center')
        welcome_label.grid(column=0, row=0, columnspan=2, sticky='N, E, W', pady=50)

        self.setup_role_selection()

    def setup_role_selection(self):

        self.role = StringVar()
        self.ROLE_OPTIONS = ["Student", "Admin"]

        intruction_label = ttk.Label(self.login_frame, text="Seleccione un rol: ", style=self.HEADER2, anchor='center')
        intruction_label.grid(column=0, row=1,sticky="W, E", padx=6)

        self.setup_login_combobox()
        self.setup_login_fields()

    def setup_login_combobox(self):

        role_combobox = ttk.Combobox(self.login_frame, textvariable=self.role, values=self.ROLE_OPTIONS, state='readonly')
        role_combobox.grid(column=1, row=1, sticky='W, E', padx=10) 
        role_combobox.current(0)
        role_combobox.bind("<<ComboboxSelected>>", self.handle_login_fields)

    def setup_login_fields(self):
    
        self.login_fields_frame = ttk.Frame(self.login_frame, width=450, height=100, style="BW.TLabel")
        self.login_fields_frame.grid(column=0, row=2, columnspan=2, pady=10)

        self.handle_login_fields()

    def handle_login_fields(self, event=None):

        self.clear_login_fields_frame()

        self.show_pass = False
        self.btn_toggle = ttk.Button(self.login_fields_frame, text="✅", command=self.toggle_password)
        self.btn_toggle.grid(column=2, row=1, sticky="W", padx=5)

        if self.role.get() == self.ROLE_OPTIONS[0]:
            self.create_login_field("Ingrese su número de carnet: ", self.student_id, self.process_login_action, 0, 0)
        else:
            self.create_login_field("Usuario: ", self.admin_user, self.process_login_action, 0, 0)
            self.create_login_field("Contraseña: ", self.admin_pass, self.process_login_action, 0, 1, "*", True)

        submit_button = ttk.Button(self.login_fields_frame, text="Submit", command=self.process_login_action)
        submit_button.grid(column=0, row=2, columnspan=2, pady=10)

    #def toggle_password(self):


    def create_login_field(self, label_text, var, command, column, row, show='', is_password=False):

        intruction_label = ttk.Label(self.login_fields_frame, text=label_text, style=self.HEADER2)
        intruction_label.grid(column=column, row=row, sticky="S", pady=5)

        entry = ttk.Entry(self.login_fields_frame, width=25, textvariable=var, show=show)
        entry.grid(column=column+1, row=row, sticky="W, E", padx=10)
        entry.bind("<Return>", lambda event: command()) # Liga el comando con la tecla Return (Enter)
        entry.focus() # Cuando es creado se selecciona

        if is_password:
            # Checkbox para mostrar/ocultar contraseña
            chk_mostrar_var = BooleanVar(value=True)  # Estado inicial como "oculto"
            mostrar_checkbox = ttk.Checkbutton(
                self.login_fields_frame, 
                text="Mostrar contraseña", 
                variable=chk_mostrar_var, 
                command=lambda: entry.config(show="*" if chk_mostrar_var.get() else "")
            )
            mostrar_checkbox.grid(column=column+1, row=row+1, sticky="W")


    def process_login_action(self):
        role_validators = {
            "Student": self.validate_student, 
            "Admin": self.validate_admin
        }
        
        selected_role = self.role.get()
        validator = role_validators.get(selected_role)

        if validator:
            input_value = self.student_id.get() if selected_role == "Estudiante" else self.manager_pass.get()
            validator(input_value)
    
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

    # ======================================== UTILITY FUNCTIONS ========================================
    def clear_login_fields_frame(self):
        
        print("Hello")
        for widget in self.login_fields_frame.winfo_children():
            widget.grid_forget()


# ======================================== RUN APP ========================================
if __name__ == "__main__":

    root_window = Tk()
    app = MainApp(root_window)
    root_window.mainloop()