class Mahasiswa:
    # konstruktor
    def __init__(self, nim, nama, rombel) :
        # variable objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    # method
    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
    
    def cetak(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Rombel :", self.rombel)

# mencetak objek
mhs1 = Mahasiswa("011022211", "Dadin", "TI05")

# mencetak atribut
mhs1.cetak()
mhs1.lulus(95)
print("="*15, "\n")

# objek 2
mhs2 = Mahasiswa("012345", "aziz bakkual", "TI05")
# mencetak atribut
mhs2.cetak()
mhs2.lulus(89)



# print(help(mhs1))