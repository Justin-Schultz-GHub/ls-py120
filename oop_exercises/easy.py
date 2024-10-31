# Banner Class
class Banner:



    def __init__(self, message, width=0):
        self.message = message
        self.width = width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        if self.width:
            return "|" + (self.width - 2) * " " + "|"

        return "|" + (len(self.message) + 2) * " " + "|"

    def _horizontal_rule(self):
        if self.width:
            return "+" + (self.width - 2) * "-" + "+"

        return "+" + (len(self.message) + 2) * "-" + "+"

    def _message_line(self):
        if self.width:
            padding_length = (self.width - len(self.message)) // 2 - 1
            padding = " " * padding_length
            return f"|{padding}{self.message}{padding}|"

        return f"| {self.message} |"


# Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 50)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('', 50)
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# Rectangle
class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height


rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True