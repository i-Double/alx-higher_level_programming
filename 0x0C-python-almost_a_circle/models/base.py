#!/usr/bin/python3
"""Module name : base, Class : Base"""


import json
import turtle


class Base:
    """Base of all other classes
        method: __init__()"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation of object argument"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of dict from json string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        for r in list_rectangles:
            rec = turtle.Turtle()
            rec.hideturtle()
            for i in range(2):
                rec.forward(r.width)
                rec.left(90)
                rec.forward(r.height)
                rec.left(90)

        for s in list_squares:
            squ = turtle.Turtle()
            squ.hideturtle()
            for i in range(2):
                rec.forward(s.size)
                rec.left(90)
                rec.forward(s.size)
                rec.left(90)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json string representation to a file"""
        fname = cls.__name__ + ".json"
        mylist = []
        if list_objs is not None and len(list_objs) != 0:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                json_dict_obj = json.loads(cls.to_json_string(obj_dict))
                mylist.append(json_dict_obj)

        with open(fname, 'w', encoding='utf-8') as wf:
            json.dump(mylist, wf)

    @classmethod
    def create(cls, **dictionary):
        """returns instance of a class with attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dummy = Square(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        fname = cls.__name__ + ".json"
        try:
            with open(fname, 'r', encoding='utf-8') as rf:
                dict_list = cls.from_json_string(rf.read())
        except Exception:
            return []

        instance_list = []
        for item in dict_list:
            temp = cls.create(**item)
            instance_list.append(temp)

        return instance_list
