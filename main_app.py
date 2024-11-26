from tkinter import *
from tkinter import ttk

from scripts.data_processing import *

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

        self.style.configure("LoginFrame.TLabel", background="grey80")
        self.style.configure("StudentMenuFrame.TLabel", background="lightCyan1")

        self.style.configure("M.TLabel", background="red")

        self.style.configure("H1.TLabel", foreground="black", font=("Consolas", 16, "bold"))
        self.style.configure("H2.TLabel", background="grey80", foreground="black", font=("Consolas", 11))
        self.style.configure("LoginErr.TLabel", background="grey80", font=("Consolas", 9, "bold"))

        self.setup_styles_constants()
    
    def setup_styles_constants(self):

        self.LOGIN_FRAME = "LoginFrame.TLabel"
        self.LOGIN_ERR = "LoginErr.TLabel"

        self.STUDENT_MENU_FRAME = "StudentMenuFrame.TLabel"

        self.HEADER1 = "H1.TLabel"
        self.HEADER2 = "H2.TLabel"

    # ======================================== LOGIN WINDOW ========================================
    def setup_login_frame(self):
        self.clear_frame(self.mainframe)
        
        self.login_frame = ttk.Frame(self.mainframe, width=500, height=300, style=self.LOGIN_FRAME)
        self.login_frame.grid(column=0, row=0)
        self.login_frame.grid_propagate(False)

        self.login_frame.columnconfigure(0, weight=1)
        self.login_frame.columnconfigure(1, weight=1)


        welcome_label = ttk.Label(self.login_frame, text="Login", style=self.HEADER1, background="grey80", anchor='center')
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
    
        self.login_fields_frame = ttk.Frame(self.login_frame, width=450, height=100, style=self.LOGIN_FRAME)
        self.login_fields_frame.grid(column=0, row=2, columnspan=2, pady=10)

        self.handle_login_fields()

    def handle_login_fields(self, event=None):

        self.clear_frame(self.login_fields_frame)

        if self.role.get() == self.ROLE_OPTIONS[0]:
            self.create_login_field("Ingrese su número de carnet: ", self.student_id, self.process_login_action, 0, 0)
        else:
            self.create_login_field("Usuario: ", self.admin_user, self.process_login_action, 0, 0)
            self.create_login_field("Contraseña: ", self.admin_pass, self.process_login_action, 0, 1, "*", True)

        submit_button = ttk.Button(self.login_fields_frame, text="Submit", command=self.process_login_action)
        submit_button.grid(column=0, row=3, columnspan=2, pady=10)

    def create_login_field(self, label_text, var, command, column, row, show='', is_password=False):

        intruction_label = ttk.Label(self.login_fields_frame, text=label_text, style=self.HEADER2)
        intruction_label.grid(column=column, row=row, sticky="S", pady=5)

        entry = ttk.Entry(self.login_fields_frame, width=25, textvariable=var, show=show)
        entry.delete(0, END)
        entry.grid(column=column+1, row=row, sticky="W, E", padx=10)
        entry.bind("<Return>", lambda event: command())
        entry.focus()

        if is_password:
            chk_show_var = BooleanVar(value=False)

            show_checkbox = ttk.Checkbutton(
                self.login_fields_frame, 
                variable=chk_show_var, 
                command=lambda: entry.config(show="" if chk_show_var.get() else "*")
            )
            show_checkbox.grid(column=column+2, row=row, sticky="W")

    def process_login_action(self):

        role_validators = {
            self.ROLE_OPTIONS[0]: self.validate_student, 
            self.ROLE_OPTIONS[1]: self.validate_admin
        }
        
        selected_role = self.role.get()
        validator = role_validators.get(selected_role)

        if validator:
            if selected_role == self.ROLE_OPTIONS[0]:
                input_value = self.student_id.get()
                validator(input_value)
            else:
                input_value1 = self.admin_user.get()
                input_value2 = self.admin_pass.get()
                validator(input_value1, input_value2)

    
    def validate_student(self, student_id_value):

        try:
            student_id_value = int(student_id_value)

            if student_id_value in self.student_table["Student ID"].values:
                self.student_name = self.student_table.loc[self.student_table["Student ID"] == student_id_value, "Name"].values[0]
                self.setup_student_frame()
            else:
                self.show_login_message("ID no encontrado.")
        except ValueError:
            self.show_login_message("Por favor ingrese un ID válido.")
        except Exception as e:
            self.show_login_message(f"Error: {e}")

    # -------------------- VALIDACIÓN DE ADMINISTRADOR --------------------
    def validate_admin(self, username, password):
        is_valid, message, user_data = validate_credentials(username, password)

        if is_valid:
            self.show_login_message(message, "green")
            self.display_admin_window()
        else:
            self.show_login_message(message)
        
    # -------------------- VALIDACIÓN DE ADMINISTRADOR --------------------
    def show_login_message(self, message, color="red"):
            
            self.clear_error_message()

            error_label = ttk.Label(self.login_fields_frame, text=message, foreground=color, style=self.LOGIN_ERR)
            error_label.grid(column=0, row=2, columnspan=2)

            self.error_message_widget = error_label
    
    # ======================================== STUDENT MAIN WINDOW ========================================
    
    def setup_student_frame(self):

        self.clear_frame(self.mainframe)
        
        self.student_frame = ttk.Frame(self.mainframe)
        self.student_frame.grid(column=0, row=0)
        self.student_frame.propagate(True)

        self.student_frame.columnconfigure(0, weight=2)
        self.student_frame.columnconfigure(1, weight=1)

        self.setup_student_menu_frame()
        self.setup_student_info_frame()

    # -------------------- STUDENT MENU FRAME --------------------

    def setup_student_menu_frame(self):

        self.student_menu_frame = ttk.Frame(self.student_frame, style=self.STUDENT_MENU_FRAME)
        self.student_menu_frame.grid(column=0, row=0)

        ttk.Button(self.student_menu_frame, command=self.setup_student_daily_menu, text="menu del día").grid(column=0, row=1)

    def setup_student_daily_menu(self):

        self.clear_frame(self.student_menu_frame)

        self.student_daily_menu_frame = ttk.Frame(self.student_menu_frame)
        self.student_daily_menu_frame.grid(column=0, row=0)

        ttk.Button(self.student_daily_menu_frame, command=print(""), text="Plato fuerte").grid(column=0, row=1)
        ttk.Button(self.student_daily_menu_frame, command=print(""), text="Ensalada").grid(column=1, row=1)
        ttk.Button(self.student_daily_menu_frame, command=print(""), text="Acompañamiento").grid(column=0, row=2)
        ttk.Button(self.student_daily_menu_frame, command=print(""), text="Ensalda").grid(column=1, row=2)

    # -------------------- STUDENT INFO FRAME --------------------

    def setup_student_info_frame(self):

        self.student_info_frame = ttk.Frame(self.student_frame, style=self.LOGIN_FRAME)
        self.student_info_frame.grid(column=1, row=0)

        ttk.Label(self.student_info_frame, text=self.student_name).grid(column=0, row=0)
        ttk.Button(self.student_info_frame, command=print("Profile"), text="Perfil").grid(column=0, row=1, rowspan=2)

        back = ttk.Button(self.student_info_frame, text="Logout", command=self.logout)
        back.grid(column=0, row=3, columnspan=2)

    # ======================================== ADMIN MAIN WINDOW ========================================

    def display_admin_window(self):

        self.clear_frame(self.mainframe)

        
        self.admin_frame = ttk.Frame(self.mainframe)
        self.admin_frame.grid(column=0, row=0)
        self.admin_frame.propagate(True)

        welcome_label = ttk.Label(self.admin_frame, text=f"Bienvenido {self.admin_user.get()}", style=self.HEADER1, background="grey80", anchor='center')
        welcome_label.grid(column=0, row=0, columnspan=2, sticky='N, E, W', pady=50)

        self.admin_frame.columnconfigure(0, weight=2)
        self.admin_frame.columnconfigure(1, weight=1)

        ttk.Button(self.admin_frame, command=print(""), text="Administrar usuarios").grid(column=0, row=1)
        ttk.Button(self.admin_frame, command=print(""), text="Ver ordenes del día").grid(column=1, row=1)



        ttk.Button(self.admin_frame, command=print(""), text="Cambiar contraseña").grid(column=2, row=3)


        back = ttk.Button(self.admin_frame, text="Logout", command=self.logout)
        back.grid(column=1, row=3)

    # ======================================== GENERAL UTILITY FUNCTIONS ========================================
    
    def logout(self):
        self.setup_login_frame()

    def clear_frame(self, frame):

        for widget in frame.winfo_children():
            widget.grid_forget()
        

    def clear_error_message(self):

        if hasattr(self, 'error_message_widget') and self.error_message_widget.winfo_ismapped():
            self.error_message_widget.grid_forget()


# ======================================== RUN APP ========================================
if __name__ == "__main__":

    root_window = Tk()
    app = MainApp(root_window)
    root_window.mainloop()