from PIL import Image
from typing import Union
import os

def get_image(path: str, width: int, height: int) -> Image.Image:
    """
    Resize an image to specified dimensions.
    
    Args:
        path (str): Path to the image file
        width (int): Desired width of the image
        height (int): Desired height of the image
    
    Returns:
        Image.Image: Resized PIL Image object
    
    Raises:
        FileNotFoundError: If the image file does not exist
        IOError: If there's an error processing the image
    """
    try:
        # Check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found: {path}")
        
        # Open and resize the image
        original_image = Image.open(path)
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        
        return resized_image
    except Exception as e:
        print(f"Error processing image {path}: {e}")
        raise