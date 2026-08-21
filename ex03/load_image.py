
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    ''' Loads an image, prints its format, and its pixels
content in RGB format.'''
    try:
        if type(path) is not str:
            raise AssertionError("path not a string.")

        im = Image.open(path).convert("RGB")
        width, height = im.size
        pix = np.array(im.get_flattened_data()).reshape(height, width, 3)
        print("The shape of image is: ", pix.shape)
        return pix

    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Error:", e)
    return None
