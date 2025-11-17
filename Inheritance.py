# contoh pewarisan dalam OOP
class Animal:
    def speak(self):
        print("Bersuara")

class Dog(Animal):  # Kelas Dog mewarisi dari kelas Animal
    def speak(self):
        print("Guk Guk!")

# Contoh penggunaan
hewan = Animal() # Membuat objek dari kelas Animal
anjing = Dog() # Membuat objek dari kelas Dog

hewan.speak()   # Output: Bersuara
anjing.speak()  # Output: Guk Guk!
