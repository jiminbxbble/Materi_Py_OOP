# Contoh enkapsulasi dalam Python
class BankAccount:
    def __init__(self, saldo):  # konstruktor
        self.__saldo = saldo    # private variable

    def deposit(self, jumlah):
        self.__saldo += jumlah  # Menambahkan jumlah ke saldo

    def lihat_saldo(self): # Getter untuk saldo
        print(f"Saldo Anda saat ini: {self.__saldo}")


# Contoh Penggunaan
akun = BankAccount(100000)  # membuat objek dengan saldo awal 100 ribu
akun.deposit(50000)         # menambah saldo
akun.lihat_saldo()          # menampilkan saldo
