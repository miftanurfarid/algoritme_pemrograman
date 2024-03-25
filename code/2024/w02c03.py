"""
Pertemuan 2 - Tugas 2
"""
from math import sqrt


a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

D = b**2 - 4*a*c

if D < 0:
    print("Akar Imajiner")
elif D == 0:
    akar = -b / (2*a)
    print("Kedua akarnya adalah {:.2f}".format(akar))
else:
    akar1 = (-b + sqrt(D)) / (2*a)
    akar2 = (-b - sqrt(D)) / (2*a)
    print("Kedua akarnya adalah {:.2f} dan {:.2f}".format(akar1, akar2))
