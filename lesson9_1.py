# ======== 1 ===========

class Car:

    def __init__(self, brand, color, engine_capacity):
        self.brand = brand
        self.color = color
        self.engine_capacity = engine_capacity

    def forward(self):
        return "move forward "

    def back(self):
        return "move back"

class AddTurnAround(Car):

    def left(self):
        return "turn left"

    def right(self):
        return  "turn right"


