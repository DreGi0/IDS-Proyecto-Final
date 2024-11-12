# Introduction to Software Engineering Final Project

This repository contains the final project for the **Introduction to Software Development** course. Below, you will find information on the team members, the necessary requirements for running the project without errors, and test credentials to explore the application's features.

## Team Members

- Debbie Nicole Cruz Alvarado
- André Giovanni Iraheta Guevara
- Tiffany Lisbeth Meléndez Ramos
- Dana Liz Ochoa González
- Oscar Marcelo Velásquez Zapata

## Developer

- André Giovanni Iraheta Guevara

## Project Requirements

This project requires a few Python libraries. Make sure the following libraries are installed in your environment:

> ⚠️ **Warning:** If you encounter issues running the project, check that these libraries are installed correctly.

> ### Windows
> ```bash
> pip install pandas bcrypt openpyxl pillow
> ```

> ### MacOS
> ```bash
> python3 -m pip install pandas bcrypt openpyxl pillow
> ```

These libraries are essential for handling password encryption and Excel file management.

> 🔴 **Important:** If you are unable to log in as a student or see the following error:
> ```
> Error loading the student data: [Errno 2] No such file or directory: 'data/students_data.xlsx'
> ```
> Please ensure that all files are in the correct project structure and that `data/students_data.xlsx` is in the specified location.

> 💡 **Tip:** Student IDs are stored in `data/students_data.xlsx`.
> 
> 💡 **Tip:** Admin profiles are stored in `data/json/admin_password.json`.

## Test Users and Passwords

To test the project functionality, you may use the following access credentials:

### Students
| **ID** |  **Name**    |
| ------ | ------------ |
| 202401 | Student1     |
| 202402 | Student2     |
| 202403 | Student3     |
|   ...  |     ...      |
| 202431 | Student31    |

### Administrators
| **Username** | **Password** |
| ------------ | ------------ |
| admin        | 123          |
| dre          | 321          |

**Note:** These credentials are only for testing purposes. If you wish to add or modify users, you can do so directly in the `students_data.xlsx` and `admin_password.json` files within the `data` folder.

---

**Fingers crossed everything works and we get a 10!**

**[GitHub Repository Link](https://github.com/DreGi0/IDS-Proyecto-Final)**
