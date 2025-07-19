from abc import ABC, abstractmethod


class Animal(ABC):

    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def eat(self):
        print(f"animal is eating....")
        pass

    def drink(self):
        print(f"animal is drinking....")
        pass