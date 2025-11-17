# Contoh enkapsulasi dalam Python
class BankAccount:
    def __init__(self, saldo): # konstruktor
        self.__saldo = saldo  # private variable

    def deposit(self, jumlah):
        self.__saldo += jumlah
        # Menambahkan jumlah ke saldo

    def lihat_saldo(self):
        print(f"Saldo Anda saat ini: {self.__saldo}")
