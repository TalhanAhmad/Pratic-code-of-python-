class Animals:
    pass



class Pets(Animals):
    pass



class Dog(Pets):
    # @staticmethod
    def bark(self):
        print(f"dad the dog is barking {"BOW BOW"}")


D = Dog()
D.bark()