from CarInventoryNode import CarInventoryNode
from Car import Car

class CarInventory:
    def __init__(self):
        self.root = None
    def addCar(self, car):
        if self.root:
            self._addCar(self.root, car)
        else:
            self.root = CarInventoryNode(car)
    def _addCar(self, node, car):
        if (node.make == car.make) and (node.model == car.model):
            node.cars.append(car)
        elif car < node.cars[0]:
            if node.left == None:
                new_node = CarInventoryNode(car)
                new_node.setParent(node)
                node.setLeft(new_node)
            else:
                self._addCar(node.left, car)
        else:
            if node.right == None:
                new_node = CarInventoryNode(car)
                new_node.setParent(node)
                node.setRight(new_node)
            else:
                self._addCar(node.right, car)
    def doesCarExist(self, car):
        return self._doesCarExist(self.root, car)
    def _doesCarExist(self, node, car):
        if node == None:
            return False
        elif (node.make == car.make) and (node.model == car.model):
            for c in node.cars:
                if c == car:
                    return True
            return False
        elif car < node.cars[0]:
            return self._doesCarExist(node.left, car)
        else:
            return self._doesCarExist(node.right, car)
    def inOrder(self):
        return self._inOrder(self.root)
    def _inOrder(self, node):
        if node != None:
            return self._inOrder(node.left) + str(node) + self._inOrder(node.right)
        return ''
    def preOrder(self):
        return self._preOrder(self.root)
    def _preOrder(self, node):
        if node != None:
            return str(node) + self._preOrder(node.left) + self._preOrder(node.right)
        return ''
    def postOrder(self):
        return self._postOrder(self.root)
    def _postOrder(self, node):
        if node is not None:
            return self._postOrder(node.left) + self._postOrder(node.right) + str(node)
        return ''
    def getBestCar(self, make, model):
        return self._getBestCar(self.root, make, model)
    def _getBestCar(self, node, make, model):
        if node is not None:
            if make.upper() == node.make and model.upper() == node.model:
                if node.cars:
                    cars = node.cars
                    cars.sort(reverse=True)
                    return cars[0]
            elif make.upper() < node.make or (make.upper() == node.make and model.upper() < node.model):
                return self._getBestCar(node.left, make, model)
            else:
                return self._getBestCar(node.right, make, model)
        return None
    def getWorstCar(self, make, model):
        return self._getWorstCar(self.root, make, model)
    def _getWorstCar(self, node, make, model):
        if node is not None:
            if make.upper() == node.make and model.upper() == node.model:
                if node.cars:
                    cars = node.cars
                    cars.sort()
                    return cars[0]
            elif make.upper() < node.make or (make.upper() == node.make and model.upper() < node.model):
                return self._getWorstCar(node.left, make, model)
            else:
                return self._getWorstCar(node.right, make, model)
        return None
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
    def _getTotalInventoryPrice(self, node):
        if node:
            sum = 0
            for car in node.cars:
                sum += car.price
            return self._getTotalInventoryPrice(node.left) + sum + self._getTotalInventoryPrice(node.right)
        else:
            return 0
    
        
