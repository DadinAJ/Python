# def sumAll(angka1,angka2,angka3,angka4):
#     total = angka1 + angka2 + angka3 + angka4
#     print(total)

# sumAll(2,2,2,2)

def sumAll(*values):
    total = 0
    for i in values:
        total += i
    print(total)

sumAll(2,3,4,1,23,2)