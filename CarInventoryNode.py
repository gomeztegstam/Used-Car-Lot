from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right
    def __str__(self):
        car_string = ''
        for car in self.cars:
            car_string += str(car) + '\n'
        return car_string
    
