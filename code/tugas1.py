# Tugas Soal 4

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("akar imajiner")
else:
    if D == 0:
        print("x1 = x2")
    else:
        if D > 0:
            print("ada dua akar dan riil")


# Tugas Soal 5
i = 1
j = 1
total = 0

while i <= 10:
    if j % 2 == 0:
        print(f"bilangan genap ke-{i} = {j}")
        total = total + j
        i = i + 1
    j = j + 1
print(f"total = {total}")
