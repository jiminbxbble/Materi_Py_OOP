#Contoh penggunaan polymorphism dalam Python
class Kucing: 
    def suara(self):
        return "Meong Meong!"

class Anjing:
    def suara(self):
        return "Guk Guk!"
    
def buat_suara(hewan):
    print(hewan.suara())

buat_suara(Kucing())  # Output: Meong Meong!
buat_suara(Anjing())  # Output: Guk Guk!