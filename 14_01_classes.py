class Rectangle:
    default_color = "green"

    def __init__(self, width, height):
        self.width = width
        self.height = height


print(Rectangle.default_color)
# print(Rectangle.width) # AttributeError: class Rectangle has no attribute 'width'
rect = Rectangle(10, 2)
print('rect.width--->' + str(rect.width))
print('rect.height--->' + str(rect.height))
