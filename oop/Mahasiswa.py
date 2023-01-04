class Mahasiswa:
    # atribut
    nama = ""
    nim = ""
    rombel = ""
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
mhs1 = Mahasiswa()
mhs1.nama = "dadin"
mhs1.nim = "0110222111"
mhs1.rombel = "T1-05"
# mencetak atribut
mhs1.cetak()
mhs1.lulus(95)
print("="*15, "\n")

# objek 2
mhs2 = Mahasiswa()
mhs2.nama = "aziz bakkual"
mhs2.nim = "0110222112"
mhs2.rombel = "T1-05"
# mencetak atribut
mhs2.cetak()
mhs2.lulus(89)



# print(help(mhs1))