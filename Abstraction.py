from abc import ABC, abstractmethod
#contoh kelas abstrak dalam OOP
class Hewan(ABC):
    @abstractmethod
    def bergerak(self):
        pass

#kelas Burung yang mewarisi dari kelas Hewan
class Burung(Hewan):
    def bergerak(self):
        print("Burung terbang di udara.")

Burung = Burung()
print(Burung.bergerak())  # Output: Burung terbang di udara.