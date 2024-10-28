import pandas as pd
import bcrypt
import json
import os

password_file_path = os.path.join("data/json", "admin_password.json")

def load_student_data(file_path):
    try:
        return pd.read_excel(file_path, sheet_name="Student_IDs")
    except Exception as e:
        print(f"Error loading the student data: {e}")
        return None


def validate_credentials(username, password):
    # Intentar cargar los usuarios del archivo JSON
    try:
        with open(password_file_path, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False, "No se encontraron usuarios o el archivo está corrupto."

    # Verificar si el usuario existe
    if username in users:
        # Obtener la contraseña cifrada del usuario
        hashed_password = users[username]['password'].encode('utf-8')
        
        # Verificar si la contraseña proporcionada coincide
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True, "Credenciales correctas."
        else:
            return False, "Contraseña incorrecta."
    else:
        return False, "Usuario no encontrado."


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