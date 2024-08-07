# street_view/photo.py
from PIL import Image
import os

class Photo:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.image = None

        if file_path:
            self.read_image(file_path)
    
    def read_image(self, file_path):
        """Read an image from a file path."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No such file: '{file_path}'")
        
        self.image = Image.open(file_path)
        print(f"Image {file_path} read successfully.")
    
    def show_image(self):
        """Display the image."""
        if self.image:
            self.image.show()
        else:
            print("No image to display.")
    def __repr__(self):
        return f"Photo(file_path={self.file_path})"
    
    def get_image_size(self):
        """Get the size (width, height) of the image."""
        if self.image:
            return self.image.size
        else:
            raise ValueError("No image loaded.")
    
    def get_file_size(self):
        """Get the file size of the image in bytes."""
        if self.file_path:
            return os.path.getsize(self.file_path)
        else:
            raise ValueError("No file path provided.")
