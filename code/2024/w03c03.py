"""
Pertemuan 3 - Tugas 3
"""

sr = float(input("Nilai skala richter dari gempa: "))

if sr >= 8:
    print("Semua bagunan rata dengan tanah")
elif sr >= 7:
    print("Banyak bangunan rusak parah")
elif sr >= 6:
    print("Beberapa bangunan rusak parah")
else:
    print("Beberapa bangunan rusak ringan")