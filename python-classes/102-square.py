#!/usr/bin/python3

"""
This module defines a Square class that represents a square shape.
It includes methods for setting and getting size, calculating area,
and comparing squares based on their area.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with an optional size (default is 0)."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality of two squares based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare inequality of two squares based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is smaller than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is smaller or equal to another based on area.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is larger than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is larger or equal to another based on area.
        """
        return self.area() >= other.area()
