#contoh pewarisan dalam OOP
class Animal:
    def speak(self):
        print("Bersuara")
    
class Dog(Animal): # Kelas Dog mewarisi dari kelas Animal
    def speak(self):
        print("Guk Guk!")