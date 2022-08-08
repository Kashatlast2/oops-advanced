from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def bark(self): pass

class Dog(AbstractAnimal):
        def bark(self):
            print('Bow Wow')

print(Dog().bark())


class Animal:

   def bark(self): pass

print(Animal ())