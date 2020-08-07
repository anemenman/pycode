class Figure(object):
    def __init__(self, color):
        self.__color = color

    # property - is decorator
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    default_color = "green"

    # Class constructor
    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super(Rectangle, cls).__new__(cls)

    # constructor
    def __init__(self, width, height, color):
        super(Rectangle, self).__init__(color)
        self.width = width
        self.height = height
        self.__private = '__private'

    # staticmethod - is decorator
    @staticmethod
    def ex_static_method():
        print("static method")

    @classmethod
    def ex_class_method(cls):
        print("class method")

    def ex_method(self):
        print("Method")
        self.__private_ex_method()

    def __private_ex_method(self):
        print("Private Method")


rect = Rectangle(2, 3, "red")
Rectangle.ex_static_method()
Rectangle.ex_class_method()
rect.ex_method()
print('rect.color()--->' + str(rect.color))
# rect.__private_ex_method() # AttributeError: Rectangle instance has no attribute '__private_ex_method'
