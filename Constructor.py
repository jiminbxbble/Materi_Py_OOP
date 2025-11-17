class Buku:
    def init (self, judul, penulis, tahun_terbit, genre): #Konstruktor yang dipanggil setiap kali objek dibuat
        self.judul = judul #variabel instance untuk menyimpan judul buku
        self.penulis = penulis #variabel instance untuk menyimpan penulis buku
        self.tahun_terbit = tahun_terbit #variabel instance untuk menyimpan tahun terbit buku
        self.genre = genre #variabel instance untuk menyimpan genre buku

    def deskripsi_buku(self):
        print(f"Judul: {self.judul}", f"Penulis: {self.penulis}", f"Tahun Terbit: {self.tahun_terbit}", f"Genre: {self.genre}", sep="\n") #Mengakses atribut instance dan variabel untuk menampilkan deskripsi buku