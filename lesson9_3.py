# ======== 3 ===========

class Parallelogram:
    def __init__(self, width, lenght):
        self.width = width
        self.length = lenght

    def get_area(self):
        return self.width*self.length

class Square(Parallelogram):

    def get_area(self):
        if self.width == self.length:
            return self.width**2
        return "це не квадрат"

A = Parallelogram(5,7)
print(A.get_area())

B = Square(5,5)
print(B.get_area())

C = Square(5,7)
print(C.get_area())