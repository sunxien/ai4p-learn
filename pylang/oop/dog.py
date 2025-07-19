from pylang.oop.animal import Animal


class Dog(Animal):

    def __init__(self, name: str):
        super().__init__(name)

    def eat(self):
        print(f"Dog {self.name} is eating....")

    def drink(self):
        print(f"Dog {self.name} is drinking....")
