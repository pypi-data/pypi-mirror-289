# street_view/photo.py
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import messagebox

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
        """Display the image in a pop-up window with resizing."""
        if self.image:
            # Resize image to 1024x768
            max_width, max_height = 1024, 768
            img_width, img_height = self.image.size

            if img_width > max_width or img_height > max_height:
                # Calculate the new size preserving the aspect ratio
                aspect_ratio = img_width / img_height
                if aspect_ratio > 1:
                    new_width = max_width
                    new_height = int(max_width / aspect_ratio)
                else:
                    new_height = max_height
                    new_width = int(max_height * aspect_ratio)
                
                self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

            # Create a Tkinter window to display the image
            root = tk.Tk()
            root.title("Image Viewer")
            img = ImageTk.PhotoImage(self.image)
            panel = tk.Label(root, image=img)
            panel.pack(side="top", fill="both", expand="yes")

            # Run the Tkinter event loop
            root.mainloop()
        else:
            print("No image to display.")
            
    def __repr__(self):
        if self.image:
            size = self.get_image_size()
            file_size = self.get_file_size()
            return (f"Photo(file_path={self.file_path}, "
                    f"size={size}, file_size={file_size} bytes)")
        else:
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
