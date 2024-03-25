"""
Pertemuan 2 - Tugas 1
"""

from math import sqrt

a = float(input("Panjang sisi siku-siku yang pertama: "))
b = float(input("Panjang sisi siku-siku yang kedua: "))
c = sqrt(a**2 + b**2)
print("Panjang sisi miring dari segitiga siku-siku adalah {:.2f}".format(c))