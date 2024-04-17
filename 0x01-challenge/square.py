#!/usr/bin/python3


class Square:
    """Square class"""

    def __init__(self, side_length):
        self.side_length = side_length  # A square only needs one side length

    def area_of_my_square(self):
        """Area of the square"""
        return self.side_length**2  # Area is side length squared

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return self.side_length * 4  # Perimeter is 4 times the side length

    def __str__(self):
        return f"Square with side length: {self.side_length}"


if __name__ == "__main__":

    s = Square(side_length=12)  # Initialize with one side length
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
