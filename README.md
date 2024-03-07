# Used-Car-Lot
Introduction
The goal for this lab is to write a program that will manage cars for a used car dealership. All cars have a make, model, year, and price, which can be used to determine the value of cars in relation to each other. All cars will be managed by a Binary Search Tree (BST) where the nodes are sorted by make, then model in lexicographical order. Within each make/model node, the Car objects will be added to a Python List based on insertion order.

In order to manage the cars for this lab, you will define Car, CarInventoryNode and CarInventory classes that organize the Cars in a BST data structure. Cars with the same make/model will be located in the same node, and appended to a list based on insertion order.

You will also write pytests in testFile.py illustrating your behavior works correctly. This lab writeup will provide some test cases for clarity, but the Gradescope autograder will run different tests shown here.

Instructions
You will need to create four files:

Car.py - Defines a Car class. This class will assume all Cars have a make(str), model(str), year(int), and a price(int).
CarInventoryNode.py - Defines a BST Node class containing all fields for a BST Node and a Python List collection of Car objects.
CarInventory.py - Defines a CarInventory (BST) class that is an ordered collection of a Dealership’s Cars. You can adapt the BST implementation shown in the textbook supporting the specifications in this lab.
testFile.py - This file will contain your pytest functions that tests the overall correctness of your class definitions.
There will be no starter code for this assignment, but rather class descriptions and required methods are defined in the specification below.

You should organize your lab work in its own directory. This way all files for a lab are located in a single folder. Also, this will be easy to import various files into your code using the import / from technique shown in lecture.

Car.py
The Car.py file will contain the definition of a Car class. The Car class will hold information about the cars (make, model, year, and price). We will define the Car attributes as follows:

make - string value representing the brand of the car (eg. Nissan, Tesla, Toyota, Ferrari). Your program must store this attribute in uppercase characters
model - string value representing the model of the car (eg. Electra, Model3, Prius, Portofino). Your program must store this attribute in uppercase characters
year - integer value representing the year of the car (eg. 2010, 2000, 1963)
price - integer value representing the price value of the car (eg. 20000, 30000, 25000)
You will write a constructor that allows the user to construct a Car object by passing in values for the make, model, year, and price.

__init__(self, make, model, year, price)
In addition to the constructor of the Car class, the following methods are required to be implemented:

__gt__(self, rhs) - comparator operator that allows us to check if a Car object is greater than another Car object. Car objects are first organized by the lexicographical/alphabetical order of their make attribute. If the make attribute is the same, then they’ll be determined by the lexicographical/alphabetical order of their model attribute. If the model attribute is the same, then they are organized by the year (from least-to-greatest). If the year is the same, then the they are organized by their price (from least-to-greatest). For example, if both Car2 and Car1 have the same make and model, then Car2 > Car1 if Car2 is newer; if Car2 and Car1 have the same year as well, then Car2 > Car1 if Car2 is more expensive.
__lt__(self, rhs) - comparator operator that allows us to check that a Car object is less than another Car object via the operation Car1 < Car2 according to the specifications above.
__eq__(self, rhs) - comparator operator that allows us to check that a Car object is equivalent to another Car (both cars have the same make, model, year, and price) via the operation Car1 == Car2.
__str__(self) - overload method that returns the details of a car via the operation str(Car1). The string representation should fit the format: "Make: [make], Model: [model], Year: [year], Price: $[price]".
For example:

c = Car("Honda", "CRV", 2007, 8000)
print(c)
Output:

Make: HONDA, Model: CRV, Year: 2007, Price: $8000
CarInventoryNode.py
The CarInventoryNode.py file will contain the definition of a CarInventoryNode class, which is the node for a BST.

The CarInventoryNode class should have the following attributes:

make - string value that represents the make of the car; just like in the Car class, your program must store this attribute in uppercase characters.
model - string value that represents the model of the car; just like in the Car class, your program must store this attribute in uppercase characters.
cars - a Python List that contains Car objects that should have the same make and model. Car objects will be organized in insertion order (most recently inserted Car will exist at the end of the Python List).
parent - a reference to the parent of a CarInventoryNode, None if it has no parent (it is the root).
left - a reference to the left child of a CarInventoryNode, None if it has no left child.
right - a reference to the right child of a CarInventoryNode, None if it has no right child.
The CarInventoryNode class should define the following methods:

__init__(self, car) - the constructor for the CarInventoryNode will take in a Car object, and initialize all attributes in the CarInventoryNode. The constructor should also append the parameter Car object from the parameter into the list attribute cars.
In addition to the construction of the BST in this class, the following methods are required to be implemented:

getMake(self) - returns a string containing the make of a CarInventoryNode.
getModel(self) - returns a string containing the model of a CarInventoryNode.
getParent(self) - returns the parent Node of the CarInventoryNode. If the parent does not exist, return None.
setParent(self, parent) - sets the parent Node of the CarInventoryNode.
getLeft(self) - returns the left child of the CarInventoryNode. If the left child does not exist, return None.
setLeft(self, left) - sets the left child of the CarInventoryNode.
getRight(self) - returns the right child of the CarInventoryNode. If the right child does not exist, return None.
setRight(self, right) - sets the right child of the CarInventoryNode.
__str__(self) - overload the string operator to allow us to get the details of all cars in the CarInventoryNode (eg, str(CarNode1)). The string representation should contain all the Car objects in this CarInventoryNode in insertion order. Make use of the Car class’ __str__ method, and separate each car with a newline character (\n) (including the last Car object in the cars Python List).
For example:

car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
print(carNode)
Output: (note the extra newline)

Make: DODGE, Model: DART, Year: 2015, Price: $6000
Make: DODGE, Model: DART, Year: 2003, Price: $5000

Some tips for the implementation:

CarInventoryNodes are ordered by make and model attributes. You can implement comparators (<, ==, >) for CarInventoryNode to help with navigating through the CarInventory, but this is not required.

CarInventory.py
The CarInventory.py file will contain the definition of a CarInventory class. This will manage the CarInventoryNodes and keep track of all the cars a dealership has. The CarInventory is implemented as a BST. The CarInventory will create and manage CarInventoryNode objects based on a car’s make and model attributes. When storing Car objects in the CarInventory, Car objects with the same make and model will be appended to a Python List based on insertion order within the CarInventoryNode object.

__init__(self) - the constructor for the CarInventory will simply initialize the empty BST. You should have an attribute called root to represent the root node of the CarInventory BST.
In addition to the construction of the BST in this class, the following methods are required to be implemented:

addCar(self, car) - adds a Car object to the BST. If a CarInventoryNode with the same make and model exists, then append the car to the end of its car list.
doesCarExist(self, car) - searches for a Car object in the CarInventory by traversing to the appropriate CarInventoryNode (if it exists), and checking the cars Python List to see if any Car object is equal to the parameter car. This method returns True if it does, and returns False otherwise (i.e. no Car object with the same make, model, year, and price exists).
inOrder(self) - returns a string with the in-order traversal of the BST. Printing the in-order traversal should help check that the cars are in the correct order in the BST
preOrder(self) - returns a string with the pre-order traversal of the BST. BSTs with the same structure should always have the same pre-order traversal, so this can be used to verify that everything was inserted correctly
postOrder(self) - returns a string with the post-order traversal of the BST.
getBestCar(self, make, model) - returns the Car with the newest year - and if multiple, then highest price - given the make and model. If the make and model doesn’t exist, then return None.
getWorstCar(self, make, model) - returns the car with the oldest year - and if multiple, then lowest price - given the make and model. If the make and model doesn’t exist, then return None.
getTotalInventoryPrice(self) - returns an integer the total price of all the cars in the dealership.
Given an example BST:

bst = CarInventory()

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)
An example of the traversal functions is given below:

assert bst.getBestCar("Nissan", "Leaf") == car1
assert bst.getBestCar("Mercedes", "Sprinter") == car3
assert bst.getBestCar("Honda", "Accord") == None

assert bst.getWorstCar("Nissan", "Leaf") == car1
assert bst.getWorstCar("Mercedes", "Sprinter") == car4
assert bst.getBestCar("Honda", "Accord") == None

assert bst.getTotalInventoryPrice() == 158000
An example of the inOrder() string format is given below:

assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
An example of the preOrder() string format is given below:

assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
An example of the postOrder() string format is given below:

assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""
Other than the required methods, feel free to implement any helper methods that you think are useful in your implementation (Gradescope will test the required methods). The automated tests will test your implementation of the required methods by creating a CarInventory containing various CarInventoryNodes containing Cars with different make, model, year, and price attributes. The addCar() method will be run, with doesCarExist(), getBestCar(), getWorstCar(), inOrder(), preOrder(), and postOrder(), etc. being used to verify that the CarInventory is fully functional. You should write similar tests to confirm your BST is working properly.
