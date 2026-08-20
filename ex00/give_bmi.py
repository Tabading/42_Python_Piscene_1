
import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    ''' Take 2 lists of integers or floats in input and
    return a list of BMI values.'''
    # bmi = weight / (heigth * height)

    try:
        if not len(height) == len(weight):
            raise AssertionError("lists not the same length")
        if not all(isinstance(x, (int | float)) for x in height) or \
                not all(isinstance(x, (int | float)) for x in weight):
            raise AssertionError("all values must be int or float")
        heights = np.array(height)
        weights = np.array(weight)
        return (weights / (heights * heights)).tolist()
    except AssertionError as e:
        print("Assertion Error:", e)
    except Exception as e:
        print("Error:", e)
    return None


def apply_limit(
    bmi: list[int | float],
    limit: int
) -> list[bool]:
    ''' Accepts a list of integers or floats and an integer
    representing a limit as parameters. It returns a list of
    booleans (True if above the limit) '''
    try:
        if not all(isinstance(x, (int | float)) for x in bmi):
            raise AssertionError("all values must be int or float")
        if type(limit) is not int:
            raise AssertionError("limit must be int")
        bmi_array = np.array(bmi)
        return (bmi_array > limit).tolist()
    except AssertionError as e:
        print("Assertion Error:", e)
    except Exception as e:
        print("Error:", e)
    return None
