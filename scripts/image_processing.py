from PIL import Image
import io

def get_image(path, width, height):
    original_image = Image.open(path)
    resized_image = original_image.resize((width, height))  # Cambia (100, 100) al tamaño deseado

    return resized_image
