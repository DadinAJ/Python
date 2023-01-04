angka = 10
for no in range(0, angka):
    no += 1
    print(no)

print("="*10)

for i in range(0, 10):
    i += 1
    if(i % 2 == 0):
        print(i)

print("="*10)

for i in range(0, 10):
    i += 1
    if(i == 9):
        continue
    print(i)