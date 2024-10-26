import os

def ensure_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def validate_student_id(student_id, student_table):
    try:
        return int(student_id) in student_table["Student ID"].values
    except ValueError:
        return False
