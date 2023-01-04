from singa import Singa
from ayam import Ayam
from sapi import Sapi

#===================================================
# Membuat Objek Harimau
singa = Singa("Singa", "Daging (Karnivora)", "Di Darat", "Melahirkan")

# print Harimau
print(f"Hewan \t\t: {singa.nama}")
print(f"Makanan \t: {singa.makanan}")
print(f"Hidup \t\t: {singa.hidup}")
print(f"Berkembang Biak : {singa.berkembang_biak}")
print("="*50, "\n")

#===================================================
# Membuat Objek Gajah
ayam = Ayam("Ayam", "Biji-bijian, serangga, dll (Omnivora)", "Di Darat", "Bertelur")

# print Gajah
print(f"Hewan \t\t: {ayam.nama}")
print(f"Makanan \t: {ayam.makanan}")
print(f"Hidup \t\t: {ayam.hidup}")
print(f"Berkembang Biak : {ayam.berkembang_biak}")
print("="*50, "\n")

#===================================================
# Membuat Objek Banteng
sapi = Sapi("Sapi", "Rumput (Herbivora)", "Di Darat", "Melahirkan")

# print Banteng
print(f"Hewan \t\t: {sapi.nama}")
print(f"Makanan \t: {sapi.makanan}")
print(f"Hidup \t\t: {sapi.hidup}")
print(f"Berkembang Biak : {sapi.berkembang_biak}")