*This project has been created as part of the 42 advanced curriculum by tabading.*

# Table of Contents
- [Description](#description)
    - [Project Specifications](#project-specifications)
    - [Mandetory Modules](#mandetory-modules)
        - [Ex00](#ex00)
        - [Ex01](#ex01)
        - [Ex02](#ex02)
        - [Ex03](#ex03)
        - [Ex04](#ex04)
        - [Ex05](#ex05)
- [Instructions](#instructions)
    - [Venv](#venv)
    - [Compilation](#compilation)
    - [Norm](#norm)
- [Resources](#resources)
    - [KI Usage](#ki-usage)


# Description
*Training Piscine Python for Data Science - 1* is the second of 5 Projects serving as an intoduction to Arrays. It encompasses 6 mandetory Modules.

### Project Specifications
For each Project these additional Rules must be followed:
- No code in the global scope. Use functions!
- Each program must have its main and not be a simple script: 

        def main():
            # your tests and your error handling

        if __name__ == "__main__":
            main()

- Any exception not caught will invalidate the exercises, even in the event of an error
that you were asked to test.
- All your functions must have documentation (\_\_doc\_\_)
- Your code must follow the norm
    - pip install flake8
    - python3 -m flake8 file.py

## Mandetory Modules

### Ex00
Learn about ***NumPy***, how to create Arrays with it and use them for fast basic calculation.

#### NumPy:
is a Python library used for working with arrays. \
It provides an array object that is:
- called ndarray
- up to 50x faster than traditional Python lists
- stored at one continuous place in memory unlike lists
- providing a lot of supporting functions
- Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result. \
    ex:

        a = np.array([20, 30, 40, 50])
        b = np.array([0, 1, 2, 3])
        c = a - b
        print(c)
            -> array([20, 29, 38, 47])

### Ex01
Learn how to manipulate a ***NumPy*** Array with the slicing method.

#### Slicing
Slicing in python means taking elements from one given index to another given index. 
- We pass slice instead of index like this: ***arr[start:end]***.
- We can also define the step, like this: ***arr[start:end:step]***.
- If we don't pass start its considered 0
- If we don't pass end its considered length of array in that dimension
- If we don't pass step its considered 1
- Negativ Slicing uses the minus operator to refer to an index from the end
- with array dimensions start on the outside going deeper:
    - arr[3D_start:3D_end, 2D_start:2D_end, start:end]

##### 1D Arrays ex:
Slice elements from index 1 to index 5 (not included):

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[1:5])
        -> [2, 3, 4, 5]

Slice elements from index 4 to the end of the array: 

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[4:])
        -> [5, 6, 7]

Slice elements from the beginning to index 4 (not included):

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[:4])
        -> [1, 2, 3, 4]

Slice from the index 3 from the end to index 1 from the end:

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[-3:-1])
        -> [5, 6]

Return every other element from index 1 to index 5:

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[1:5:2])
        -> [2, 4]

##### 2D Arrays ex:
From the second element, slice elements from index 1 to index 4 (not included):

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr[1, 1:4])
        -> [7, 8, 9]

From both elements, return index 2:

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr[0:2, 2])
        -> [3, 8]

From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr[0:2, 1:4]) # same as arr[0:, 1:4]
        -> [[2, 3, 4], [7, 8, 9]]

### Ex02
Independently find a Library for the task, use PIL Image to work with Images and reshape ***NumPy*** Arrays. 

#### PIL Image Module:
The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.

### Ex03
Using the ***matplotlib*** library to display a grid with a pix array gotten from PIL.

#### matplotlib display an Image:

    plt.imgplot = plt.imshow(img, cmap='gray')
    plt.show()


### Ex04

### Ex05

# Instructions

### Venv
Create a Venv with all required libs, unless you want to install them  globaly.

- python3 -m venv venv
- source venv/bin/activate
- pip install numpy
- pip install pillow
- pip install flake8
- deactivate (to exit)


### Compilation

    python3 *.py

### Norm 

    python3 -m flake8 *.py

# Resources
ex00:
- https://www.w3schools.com/python/numpy/numpy_intro.asp
- https://numpy.org/devdocs/user/quickstart.html
- https://www.geeksforgeeks.org/numpy/python-numpy/

ex01:
- https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
- https://numpy.org/devdocs/user/quickstart.html
- https://www.w3schools.com/python/numpy/numpy_array_shape.asp

ex02:
- https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
- https://pillow.readthedocs.io/en/stable/reference/Image.html

ex03:
- https://pillow.readthedocs.io/en/stable/reference/Image.html#
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow
- KI to help find the relevant information in the library documentations

ex04:

ex05:

### KI Usage
KI was generally used to save time searching for specific functions, explaining specifics, figuring out what what i'm trying to do is called and finding shorter solutions, ie. how MY code could be reformated to be shorter/less lines for learning purposes.