class Shape:
    def __init__(self, color=''):
        self.color = color
    def area(self):
        return 0
    def perimeter(self):
        return 0
    def __str__(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, color='', width=0.0, height=0.0):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2* (self.width + self.height)
    def __str__(self):
        return self.width, self.height
    
test = Shape('purple')
print(test)
print(test.area())
print(test.perimeter())

test2 = Rectangle('purple', 4, 5)
print(test2.area())
print(test2.perimeter())