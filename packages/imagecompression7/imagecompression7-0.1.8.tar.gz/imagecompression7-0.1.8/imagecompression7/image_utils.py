from PIL import Image
import numpy as np

def load_image(image_path):
    return Image.open(image_path).convert('L')

def image_to_matrix(image):
    return np.asarray(image)

def matrix_to_image(matrix):
    return Image.fromarray(matrix.astype('uint8'))

def save_image(image, path):
    image.save(path)
