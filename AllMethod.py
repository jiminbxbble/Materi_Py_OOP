# contoh berbagai jenis method dalam OOP
class Calculator:
    total_instance = 0  # Variabel kelas untuk melacak total instance yang dibuat

    def __init__(self, value):
        self.value = value  # Variabel instance
        Calculator.total_instance += 1

    # Instance method
    def add(self, number):
        self.value += number
        return self.value
    
    # Class method
    @classmethod
    def get_instance_count(cls):
        return cls.total_instance
    
    # Static method
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    # Dunder method
    def __str__(self):
        return f"Calculator(value: {self.value})"
    

# Contoh penggunaan kelas Calculator
calc1 = Calculator(10)
calc2 = Calculator(20)

print(calc1.add(5))                 # Instance method
print(Calculator.is_even(4))        # Static method
print(Calculator.get_instance_count())  # Class method
print(calc1)                        # __str__ (dunder) method
