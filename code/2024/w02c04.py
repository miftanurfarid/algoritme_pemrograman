"""
Pertemuan 2 - Tugas 2
"""

counter = 0
total = 0

for bilangan in range(1,100):
    if bilangan % 2 == 0:
        total += bilangan
        counter += 1
        print(f"Bilangan genap ke-{counter} adalah {bilangan}")
    
    if counter == 10:
        break

print(f"\nTotal penjumlahannya adalah {total}")
