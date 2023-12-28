import sys
sys.path.append('/Users/annakulievadiana/Desktop/lab2/')

import numpy as np
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    rectangle = Rectangle(3, 9, "blue")
    circle = Circle(3, "green")
    square = Square(3, "red")

    print(rectangle)
    print(circle)
    print(square)

    print(np.version.version)

if __name__ == "__main__":
    main()


