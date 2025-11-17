# contoh penggunaan variabel kelas, variabel private dan variabel instance dalam OOP
class Student:
    school_name = "Telkom University"      # Variabel kelas
    __id_counter = 1                       # Private class variable untuk auto-number ID

    def __init__(self, name, age):
        self.name = name
        self.age = age                     # Variabel instance

        # Buat private ID berdasarkan counter
        self.__student_id = Student.__id_counter  
        Student.__id_counter += 1          # Increment setiap kali instance dibuat

    def get_student_id(self):
        return f"{self.name} student id is {self.__student_id}"  # Getter untuk ID private


# Membuat objek
s1 = Student("Park Jisung", 20)
s2 = Student("Zhong Chenle", 21)

print(Student.school_name)
print(s1.name, s1.age)
print(s2.name, s2.age)
print(s1.get_student_id())   # Output: 1
print(s2.get_student_id())   # Output: 2
