# Street View Image Processing and Solar Loaction Library

This library provides a `Photo` class to handle basic street view image processing tasks, including reading images, displaying them, and retrieving image file details.

## Features

- Read and display images
- Get image dimensions (width and height)
- Get image file size

## Installation

1. Ensure you have Python installed.
2. Install the Pillow library if you haven't already:

   ```bash
   pip install pillow
   ```
3. Download or clone this repository.
4. Include the street_view directory in your project.

## Usage
Here is a basic example of how to use the `Photo` class:
```python
from StreetSolarTrack.utils.photo import Photo

# Create a Photo instance and read an image
photo = Photo('path_to_your_image.jpg')

# Display the object's string representation
print(photo)

# Show the image
# photo.show_image()


# Get and print the image dimensions
print(f"Image size (width, height): {photo.get_image_size()}")

# Get and print the file size
print(f"File size (bytes): {photo.get_file_size()}")

```
## API Documentation

## API Documentation

### `Photo`

#### `__init__(self, file_path=None)`

Initialize a `Photo` instance.

- `file_path` (str, optional): The path to the image file. If provided, the image will be read during initialization.

#### `read_image(self, file_path)`

Read an image from a file path.

- `file_path` (str): The path to the image file.

Raises:
- `FileNotFoundError`: If the file does not exist.

#### `show_image(self)`

Display the image using the default image viewer.

#### `get_image_size(self)`

Get the size (width, height) of the image.

Returns:
- Tuple (int, int): The width and height of the image.

Raises:
- `ValueError`: If no image is loaded.

#### `get_file_size(self)`

Get the file size of the image in bytes.

Returns:
- int: The file size in bytes.

Raises:
- `ValueError`: If no file path is provided.

#### `__repr__(self)`

Return a string representation of the `Photo` instance.


## Dev
This lib is build under the guide of :
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
  - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml

