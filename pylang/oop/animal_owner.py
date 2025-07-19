from pylang.oop.animal import Animal
from pylang.oop.cat import Cat
from pylang.oop.dog import Dog


class AnimalOwner:

    def __init__(self):
        pass

    def feed_food(self, animal: Animal):
        animal.eat()

    def feed_water(self, animal: Animal):
        animal.drink()


if __name__ == "__main__":
    dog = Dog("Doggie")
    cat = Cat("Sophie")

    animal_owner = AnimalOwner()
    animal_owner.feed_food(dog)
    animal_owner.feed_water(dog)

    animal_owner.feed_food(cat)
    animal_owner.feed_water(cat)
