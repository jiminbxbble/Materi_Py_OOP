class Buku:
    def __init__(self, judul, penulis, tahun_terbit, genre):  # Konstruktor
        self.judul = judul #variabel instance untuk menyimpan judul buku
        self.penulis = penulis #variabel instance untuk menyimpan penulis buku
        self.tahun_terbit = tahun_terbit #variabel instance untuk menyimpan tahun terbit buku
        self.genre = genre #variabel instance untuk menyimpan genre buku

    def deskripsi_buku(self): #method untuk menampilkan deskripsi buku
        print(
            f"Judul: {self.judul}", #variabel instance untuk menampilkan judul buku
            f"Penulis: {self.penulis}", #variabel instance untuk menampilkan penulis buku
            f"Tahun Terbit: {self.tahun_terbit}", #variabel instance untuk menampilkan tahun terbit buku
            f"Genre: {self.genre}", #variabel instance untuk menampilkan genre buku
            sep="\n" #separator agar setiap atribut tidak ada dalam satu baris
        )

# Contoh penggunaan
b1 = Buku("Laut Bercerita", "Leila S. Chudori", 2017, "Fiksi") #membuat objek b1 dari kelas Buku
b1.deskripsi_buku() #memanggil method deskripsi_buku untuk objek b1
