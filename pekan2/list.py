# # membuat list ditandai dengan []
buah = ["mangga", "melon", "jeruk", "apel"]
print(buah[3])

# # menambah list dengan append("value")
buah.append("pisang")
print(buah)

# # mengubah list
# # variabel[index ke berapa] = nilai baru
buah[0] = "jambu"
print(buah)

# # menghapus list
# # del buah[index yang mau dihapus]
del buah[1]
print(buah)

# # mengambil data akhir dengan pop
print(buah.pop())

# # mengetahui jumlah data dari list
# # menggunakan len()
print(len(buah))

# # menyisipkan data sesuai yang diinginkan
# # menggunakan insert(index, value)
buah.insert(1,"duku")
print(buah)

# # mengambil seluruh data di list menggunakan perulangan for
for a in buah:
    print(a)