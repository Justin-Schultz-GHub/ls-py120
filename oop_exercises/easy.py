# # Banner Class
# class Banner:



#     def __init__(self, message, width=0):
#         self.message = message
#         self.width = width

#     def __str__(self):
#         return "\n".join([self._horizontal_rule(),
#                           self._empty_line(),
#                           self._message_line(),
#                           self._empty_line(),
#                           self._horizontal_rule()])

#     def _empty_line(self):
#         if self.width:
#             return "|" + (self.width - 2) * " " + "|"

#         return "|" + (len(self.message) + 2) * " " + "|"

#     def _horizontal_rule(self):
#         if self.width:
#             return "+" + (self.width - 2) * "-" + "+"

#         return "+" + (len(self.message) + 2) * "-" + "+"

#     def _message_line(self):
#         if self.width:
#             padding_length = (self.width - len(self.message)) // 2 - 1
#             padding = " " * padding_length
#             return f"|{padding}{self.message}{padding}|"

#         return f"| {self.message} |"


# # Comments show expected output

# banner = Banner('To boldly go where no one has gone before.', 50)
# print(banner)
# # +--------------------------------------------+
# # |                                            |
# # | To boldly go where no one has gone before. |
# # |                                            |
# # +--------------------------------------------+

# banner = Banner('', 50)
# print(banner)
# # +--+
# # |  |
# # |  |
# # |  |
# # +--+

# # Rectangle
# class Rectangle:

#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height


# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

# # Rectangles and Squares
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height



# class Square(Rectangle):

#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)


# square = Square(5)
# print(square.area == 25)      # True


# # Complete the Program - Cats!
# class Pet:
#     def __init__(self, name, age, color):
#         self._name = name
#         self._age = age
#         self._color = color

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @property
#     def color(self):
#         return self._color

# class Cat(Pet):

#     @property
#     def info(self):
#         return f'My cat {self.name} is {self.age} years old and has {self.color} fur.'

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)


# # Animals
# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (f"Hello, my name is {self.name} and I am "
#                 f"{self.age} years old and {self.status}.")


# class Cat(Animal):

#     SOUND = "Meow meow!"

#     def __init__(self, name, age, status):
#         super().__init__(name, age, 4, "cat", status)

#     def introduce(self):
#         return f"{super().introduce()} {self.SOUND}"


# class Dog(Animal):

#     SOUND = "Woof! Woof!"

#     def __init__(self, name, age, status, owner):
#         self.owner = owner
#         super().__init__(name, age, 4, "dog", status)

#     def introduce(self):
#         return f"{super().introduce()} {self.SOUND}"

#     def greet_owner(self):
#         return f"Hi {self.owner}! {self.SOUND}"


# cat = Cat("Pepe", 4, "happy")
# expected = ("Hello, my name is Pepe and I am 4 years old "
#             "and happy. Meow meow!")
# print(cat.introduce() == expected)      # True

# dog = Dog("Bobo", 9, "hungry", "Daddy")
# expected = ("Hello, my name is Bobo and I am 9 years old "
#             "and hungry. Woof! Woof!")
# print(dog.introduce() == expected)                  # True
# print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True


# # Pet Shelter
# class Pet:
#     def __init__(self, species, name):
#         self.species = species
#         self.name = name

#     def info(self):
#         return f"A {self.species} named {self.name}."

# class Owner:
#     def __init__(self, name):
#         self.name = name
#         self.pets = []

#     def add_pet(self, pet):
#         self.pets.append(pet)

#     def number_of_pets(self):
#         return len(self.pets)

#     def print_pets(self):
#         for pet in self.pets:
#             print(pet.info())

# class Shelter:
#     def __init__(self):
#         self.adoptions = {}

#     def adopt(self, owner, pet):
#         owner.add_pet(pet)

#         self.adoptions[owner.name] = owner

#     def print_adoptions(self):
#         for name, owner in self.adoptions.items():
#             print(f"{name} has adopted the following pets:")
#             owner.print_pets()

#             print("")

# cocoa   = Pet('cat', 'Cocoa')
# cheddar = Pet('cat', 'Cheddar')
# darwin  = Pet('bearded dragon', 'Darwin')
# kennedy = Pet('dog', 'Kennedy')
# sweetie = Pet('parakeet', 'Sweetie Pie')
# molly   = Pet('dog', 'Molly')
# chester = Pet('fish', 'Chester')

# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")


# # Refactoring Vehicles
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def info(self):
#         return f"{self.make} {self.model}"

#     def get_wheels(self):
#         return 4


# class Car(Vehicle):
#     pass


# class Motorcycle(Vehicle):
#     def get_wheels(self):
#         return 2


# class Truck(Vehicle):
#     def __init__(self, make, model, payload):
#         super().__init__(make, model)
#         self.payload = payload

#     def get_wheels(self):
#         return 6

# class Quad(Vehicle):
#     pass


# car = Car("Honda", "Accord")
# motorcycle = Motorcycle("Kawasaki", "Ninja")
# truck = Truck("Dodge", "Mammoth", 2300)
# quad = Quad("Polaris", "Sportsman 850")

# vehicles = [car, motorcycle, truck, quad]
# methods = ["make", "model", "get_wheels", "payload"]

# for vehicle in vehicles:
#     for method in methods:
#         if method == "get_wheels":
#                 print(getattr(vehicle, method)())
#         else:
#             try:
#                 print(getattr(vehicle, method))

#             except AttributeError:
#                 pass

#     print()


# # Moving
# class WalkMixIn:
#     def walk(self):
#         return f'{self.name} {self.gait()} forward'

# class Person(WalkMixIn):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

# class Cat(WalkMixIn):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

# class Cheetah(WalkMixIn):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"


# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"


# # Nobility
# class WalkMixIn:
#     def walk(self):
#         return f'{self} {self.gait()} forward'

# class Person(WalkMixIn):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

#     def __str__(self):
#         return self.name

# class Cat(WalkMixIn):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

#     def __str__(self):
#         return self.name

# class Cheetah(WalkMixIn):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"

#     def __str__(self):
#         return self.name

# class Noble(WalkMixIn):
#     def __init__(self, name, title):
#         self.name = name
#         self.title = title

#     def gait(self):
#         return "struts"

#     def __str__(self):
#         return f'{self.title} {self.name}'

# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# byron = Noble("Byron", "Lord")
# print(byron.walk())  # "Lord Byron struts forward"
# print(byron.name)    # "Byron"
# print(byron.title)   # "Lord"


# # Complete the Program - Houses!
# class House:
#     def __init__(self, price):
#         self._price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

#     def __gt__(self, other):
#         if isinstance(other, House):
#             return self._price > other._price

#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, House):
#             return self._price < other._price

#         return NotImplemented

# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")


# # Wallet (Part 1)
# class Wallet:

#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         if isinstance(other, Wallet):
#             return Wallet(self.amount + other.amount)

#         return NotImplemented

# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet.amount == 80)       # True


# # Wallet (Part 2)
# class Wallet:

#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         if isinstance(other, Wallet):
#             return Wallet(self.amount + other.amount)

#         return NotImplemented

#     def __str__(self):
#         return f'Wallet with ${self.amount}.'


# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet)          # Wallet with $80.


# # Reverse Engineering
# class Transform:
#     def __init__(self, chars):
#         self.chars = chars

#     def uppercase(self):
#         return self.chars.upper()

#     @classmethod
#     def lowercase(cls, chars):
#         return chars.lower()

# my_data = Transform('abc')
# print(my_data.uppercase())              # ABC
# print(Transform.lowercase('XYZ'))       # xyz

