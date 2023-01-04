# membuat dictionary { key : value }

data = {"nama":"Dadin Ahmad Jamaludin"}
print(data["nama"])
print("="*20)

# memanggil key nya aja
nilai = {"firda":89, "inaya":80, "fawwaz":95, "rahmah":100}
for angka in nilai.keys():
    print(angka)
print("="*20)

# memanggil value nya aja
for angka in nilai.values():
    print(angka)
print("="*20)

for nama,nilai in nilai.items():
    print(nama, " : ", nilai)