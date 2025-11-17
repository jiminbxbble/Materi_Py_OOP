from abc import ABC, abstractmethod
#contoh kelas abstrak, pewarisan, enkapsulasi, dan polimorfisme dalam OOP
class Animal(ABC):
    #Contoh class variable
    species_count = 0

    def __init__(self, name, age): #kosntruktor
        #Contoh instance variable
        self.name = name
        self.age = age

        #Contoh private variable (Enkapsulasi)
        self.__id = f"{name.lower()} is {age}"

        Animal.species_count += 1

    #Contoh abstract method (Abstraksi)
    @abstractmethod
    def make_sound(self):
        pass

    #Contoh instance method
    def info(self):
        return f"{self.name} is {self.age} years old."

    #Contoh class method
    @classmethod
    def get_species_count(cls):
        return cls.species_count

    #Contoh static method
    @staticmethod
    def is_adult(age):
        return age >= 1

    #Contoh getter (Enkapsulasi)
    def get_id(self):
        return self.__id

    #Contoh dunder method (Polimorphism)
    def __str__(self):
        return f"Animal(name: {self.name}, age: {self.age})"

#contoh inheritance dari kelas Animal
class Dog(Animal):
    # Polymorphism: implementasi berbeda dari make_sound()
    def make_sound(self):
        return f"{self.name}Woof!"

    # Override dunder method (polymorphism)
    def __str__(self):
        return f"Dog(name: {self.name}, age: {self.age})"


class Cat(Animal):
    # Polymorphism: implementasi berbeda lagi
    def make_sound(self):
        return f"{self.name} Meow!"

    def __str__(self):
        return f"Cat(name: {self.name}, age: {self.age})"

# Contoh penggunaan kelas dan metode
dog = Dog("Jaejae", 3)
cat = Cat("Mimi", 2)

print(dog.info())              # Instance method
print(cat.make_sound())        # Polymorphism (method berbeda)
print(Animal.get_species_count())  # Class method
print(Animal.is_adult(2))      # Static method
print(dog.get_id())            # Akses private variable lewat getter
print(dog)                     # __str__()
print(cat)
