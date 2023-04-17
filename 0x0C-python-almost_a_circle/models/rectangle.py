#!/usr/bin/python3
"""Module name : rectangle, Class : Rectangle"""


from models.base import Base


import json


class Rectangle(Base):
    """Defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Shows a visual representation of the rectangle"""
        for d in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(self.__x * ' ', self.__width * '#'))

    def __str__(self):
        """Returns string representation of object"""
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                 self.__x, self.__y,
                                                 self.__width,
                                                 self.__height))

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        if (len(args) != 0):
            attr = ["id", "width", "height", "x", "y"]
            n = 0
            for x in args:
                self.__setattr__(attr[n], x)
                n += 1
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle class"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
