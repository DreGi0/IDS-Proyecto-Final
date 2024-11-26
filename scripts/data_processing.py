import pandas as pd
import bcrypt
import json
import os

password_file_path = os.path.join("data/json", "admin_password.json")
orders_file_path = os.path.join("data/json", "orders.json")

# ======================================== STUDENT DATA ========================================
def load_student_data(file_path):
    try:
        return pd.read_excel(file_path, sheet_name="Student_IDs")
    except Exception as e:
        print(f"Error loading the student data: {e}")
        return None

def get_student_name_by_id(student_data, student_id):
    try:
        name = student_data.loc[student_data['Student ID'] == student_id, 'Name'].values
        if len(name) > 0:
            return name[0]
        else:
            return None
    except Exception as e:
        print(f"Error fetching name for ID {student_id}: {e}")
        return None

# ======================================== ADMIN DATA ========================================
def validate_credentials(username, password):
    try:
        with open(password_file_path, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False, "No se encontraron usuarios o el archivo está corrupto.", None

    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            # Returns True, success message, and user data
            return True, "Credenciales correctas.", {
                "name": username,
                "email": users[username]['email']
            }
        else:
            # Invalid password
            return False, "Contraseña incorrecta.", None
    else:
        # User not found
        return False, "Usuario no encontrado.", None

def save_admin_credentials(username, password, email=None):

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user_data = {
        username: {
            'password': hashed_password.decode('utf-8'),
            'email': email
        }
    }

    try:
        with open(password_file_path, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    users.update(user_data)

    with open(password_file_path, 'w') as f:
        json.dump(users, f, indent=4)

def update_password(username, new_password):

    try:
        with open(password_file_path, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se encontraron usuarios o el archivo está corrupto.")
        return

    if username in users:
        # Cifrar la nueva contraseña
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        
        # Actualizar la contraseña del usuario
        users[username]['password'] = hashed_password.decode('utf-8')

        # Guardar el diccionario actualizado en el archivo JSON
        with open(password_file_path, 'w') as f:
            json.dump(users, f, indent=4)

        print(f"Contraseña de {username} actualizada con éxito.")
    else:
        print(f"Usuario {username} no encontrado.")

# ======================================== ORDERS DATA ========================================
def save_student_order(st_name, st_id, plate, salad, drink, accompaniment):
    order_data = {
        f"{st_id} {st_name}": {
            'Plate': plate,
            'Accompaniment': accompaniment,
            'Salad': salad,
            'Drink': drink
        }
    }

    try:
        with open(orders_file_path, 'r') as f:
            orders = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        orders = {}

    orders.update(order_data)

    with open(orders_file_path, 'w') as f:
        json.dump(orders, f, indent=4)

def delete_student_ordes():
    with open(orders_file_path, 'w') as f:
        json.dump({}, f)

def format_student_data(student_data):
    formatted_data = []
    try:
        # Iterar sobre cada fila y añadir cada registro como un subarray
        for index, row in student_data.iterrows():
            formatted_data.append([
                row['Student ID'],
                row['Name'],
                bool(row['Scholarship'])  # Convierte a bool para indicar si tiene beca o no
            ])
    except KeyError:
        print("Error: asegúrate de que las columnas 'Student ID', 'Name' y 'Scholarship' existen en el archivo de Excel.")
    except Exception as e:
        print(f"Error al procesar los datos de estudiantes: {e}")
    return formatted_data

def get_all_orders():
    try:
        # Cargar los pedidos desde el archivo JSON
        with open(orders_file_path, 'r') as f:
            orders = json.load(f)
        
        # Formatear cada pedido en un array con la estructura deseada
        formatted_orders = []
        for student_key, order_details in orders.items():
            # Extraer el ID del estudiante del nombre de clave (por ejemplo, "202401 Estudiante 1")
            student_id = student_key.split()[0]
            # Extraer la información y formatearla
            formatted_orders.append([
                student_id,
                order_details.get("Plate"),
                order_details.get("Salad"),
                order_details.get("Accompaniment"),
                order_details.get("Drink")
            ])
        return formatted_orders
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading orders data: {e}")
        return []