
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def ft_zoom(path: str) -> np.ndarray:
    ''' Turn the Image into Grayscale, splice the array \
    to a zoomed in area, display the new Image in a grid and \
    return the pixel array '''
    try:
        # open img and convert to grayscale
        img = Image.open(path).convert("L")
        w, h = img.size
        pix = np.array(img.get_flattened_data()).reshape(h, w, 1)

        # splice the pix array to the zoomed in area
        zo = pix[100:500, 450:850, :]

        # print new shape and array
        print("New shape after slicing:", zo.shape, "or", zo.shape[:2])
        plt.imgplot = plt.imshow(zo, cmap='gray')

        return zo
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Error:", e)


def main():
    # display rgb pix grid with ft_load
    print(ft_load("animal.jpeg"))
    print(ft_zoom("animal.jpeg"))

    # display img in grid
    plt.show()


if __name__ == "__main__":
    main()
