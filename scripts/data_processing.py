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

def save_orders(order_file, orders):
    with open(order_file, "w") as f:
        json.dump(orders, f, indent=4)

def load_orders(order_file):
    if os.path.exists(order_file):
        with open(order_file, "r") as f:
            return json.load(f)
    return []

def save_admin_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    with open(password_file_path, 'w') as f:
        json.dump({'password': hashed.decode('utf-8')}, f)

def load_admin_password():
    if os.path.exists(password_file_path):
        with open(password_file_path, 'r') as f:
            data = json.load(f)
            return data['password'].encode('utf-8')
    return None

def compare_password(password):
    return load_admin_password() and bcrypt.checkpw(password.encode('utf-8'), load_admin_password())