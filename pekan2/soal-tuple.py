# membuat tuple menggunakan buka tutup kurung ("value", ...)
gorengan = ('bakwan','combro','misro')
sop = ('sop iga', 'sop buntut', 'sop kaki')
nasi = ('nasi uduk','nasi goreng','nasi remes')
# tuple di dalam tuple
makanan = (gorengan, sop, nasi)

# cetak gorengan dri v makanan
for i in makanan[0]:
    print(i)

print("="*10)
print(makanan[2][2])

print("="*10)
for i in makanan:
    for a in i:
        print(a)