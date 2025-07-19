from pylang.oop.animal import Animal


class Cat(Animal):

    def __init__(self, name: str):
        super().__init__(name)

    def eat(self):
        print(f"Cat {self.name} is eating....")

    def drink(self):
        print(f"Cat {self.name} is drinking....")
