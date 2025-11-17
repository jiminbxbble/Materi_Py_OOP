#contoh penggunaan variabel kelas, variabel private dan variabel instance dalam OOP
class Student:
    school_name = "Telkom University"  # Variabel kelas yang dimiliki bersama oleh semua instance

    def __init__(self, name, age):
        self.name = name
        self.age = age  # Variabel instance yang unik untuk setiap instance

        self.__student_id = f"ID-{name.lower()}"  # Variabel private untuk menyimpan ID siswa

    def get_student_id(self):
        return self.__student_id  # Metode untuk mengakses variabel private
        
s1 = Student("Jisung", 20)
s2 = Student("Chenle", 21)

print(Student.school_name)  # Output: Telkom University
print(s1.name, s1.age)      # Output: Jisung, 20
print(s2.name, s2.age)      # Output: Chenle, 21
print(s1.get_student_id())  # Akses private variabel