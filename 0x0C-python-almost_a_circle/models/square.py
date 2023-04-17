#!/usr/bin/python3
"""Module name : square, Class : Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialises instance attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for width of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of object"""
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                              self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        """Assigns keyworded attributes"""
        if (len(args) != 0):
            attr = ["id", "size", "x", "y"]
            n = 0
            for value in args:
                self.__setattr__(attr[n], value)
                n += 1
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "width"),
                'y': getattr(self, "y")}
