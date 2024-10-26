from tkinter import *
from tkinter import ttk

# Crear ventana principal
window = Tk()

# Crear un Frame con tamaño fijo (200x100)
container_frame = Frame(window, bg="Black", width=200, height=100)
container_frame.grid(row=0, column=0, padx=10, pady=10)

container_frame.grid_propagate(True)

def create_frame(parent, color, width, height, column, row, padx, pady,propagate=True):
    new_frame = Frame(parent, bg=color, width=width, height=height)
    new_frame.grid(column=column, row=row, padx=padx, pady=pady)

    new_frame.grid_propagate(propagate)

    return new_frame

parent_1 = create_frame(window, "Black", 130, 330, 0, 0, 10, 10)
parent_2 = create_frame(window, "Black", 110, 330, 1, 0, 10, 10)
parent_3 = create_frame(window, "Black", 110, 330, 2, 0, 10, 10)

child_1_1 = create_frame(parent_1, "Red", 100, 100, 0, 0, 10, 10)
child_2_1 = create_frame(parent_1, "Green", 100, 100, 0, 1, 10, 10)
child_3_1 = create_frame(parent_1, "Blue", 100, 100, 0, 2, 10, 10)

child_4_1 = create_frame(parent_1, "Red", 100, 100, 1, 0, 10, 10)
child_5_1 = create_frame(parent_1, "Green", 100, 100, 1, 1, 10, 10)
child_6_1 = create_frame(parent_1, "Blue", 100, 100, 1, 2, 10, 10)

child_7_1 = create_frame(parent_1, "Red", 100, 100, 2, 0, 10, 10)
child_8_1 = create_frame(parent_1, "Green", 100, 100, 2, 1, 10, 10)
child_9_1 = create_frame(parent_1, "Blue", 100, 100, 2, 2, 10, 10)



child_1_2 = create_frame(parent_2, "Red", 100, 100, 0, 0, 10, 10)
child_2_2 = create_frame(parent_2, "Green", 100, 100, 0, 1, 10, 10)
child_3_2 = create_frame(parent_2, "Blue", 100, 100, 0, 2, 10, 10)

child_4_2 = create_frame(parent_2, "Red", 100, 100, 1, 0, 10, 10)
child_5_2 = create_frame(parent_2, "Green", 100, 100, 1, 1, 10, 10)
child_6_2 = create_frame(parent_2, "Blue", 100, 100, 1, 2, 10, 10)

child_7_2 = create_frame(parent_2, "Red", 100, 100, 2, 0, 10, 10)
child_8_2 = create_frame(parent_2, "Green", 100, 100, 2, 1, 10, 10)
child_9_2 = create_frame(parent_2, "Blue", 100, 100, 0, 2, 10, 10)



child_1_3 = create_frame(parent_3, "Red", 100, 100, 0, 0, 10, 10)
child_2_3 = create_frame(parent_3, "Green", 100, 100, 0, 1, 10, 10)
child_3_3 = create_frame(parent_3, "Blue", 100, 100, 0, 2, 10, 10)

child_4_3 = create_frame(parent_3, "Red", 100, 100, 0, 0, 10, 10)
child_5_3 = create_frame(parent_3, "Green", 100, 100, 0, 1, 10, 10)
child_6_3 = create_frame(parent_3, "Blue", 100, 100, 0, 2, 10, 10)

child_7_3 = create_frame(parent_3, "Red", 100, 100, 0, 0, 10, 10)
child_8_3 = create_frame(parent_3, "Green", 100, 100, 0, 1, 10, 10)
child_9_3 = create_frame(parent_3, "Blue", 100, 100, 0, 2, 10, 10)



# Añadir una etiqueta dentro del Frame
label = Label(container_frame, text="Texto dentro del Frame", bg="white")
label.grid(row=0, column=0)

window.grid_propagate(True)

# Ejecutar la aplicación
window.mainloop()