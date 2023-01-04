# Buat fungsi untuk menampilkan nama2 siswa yang lulus
# dari hasil_akhir di slide sebelumnya (nilai > 65)

hasil_akhir = [
    {'nama':'Reza', 'nilai':70}, #index ke -0
    {'nama':'Ciut', 'nilai':63}, #index ke -1 
    {'nama':'Dian', 'nilai':80}, #index ke -2
    {'nama':'Badu', 'nilai':40}  #index ke -3
]

def lulus(data):
    for i in data:
        if i['nilai'] > 65:
            print(i['nama'])

lulus(hasil_akhir)