
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    ''' Takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and
end arguments '''
    try:
        if type(family) is not list:
            raise AssertionError("not a list.")
        if type(start) is not int or type(end) is not int:
            raise AssertionError("not an int.")
        arr = np.array(family)
        print("my shape is:", arr.shape)
        spl = arr[start:end, :]
        print("my new shape is:", spl.shape)
        return spl.tolist()
    except AssertionError as e:
        print("Assertion Error:", e)
    except Exception as e:
        print("Error:", e)
    return None
