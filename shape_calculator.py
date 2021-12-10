class Rectangle(object):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        result = []
        if(self.height > 50 or self.width > 50):
            result = 'Too big for picture.'
        else:
            for h in range(self.height):
                line = '*' * self.width
                result.append(line)
            result.append('')
            result =  '\n'.join(result)
        return result

    def get_amount_inside(self, shape):
        return int(self.get_area()/shape.get_area())

    def __str__(self) -> str:
        return 'Rectangle(width={0}, height={1})'.format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def __str__(self) -> str:
        return 'Square(side={0})'.format(self.width)