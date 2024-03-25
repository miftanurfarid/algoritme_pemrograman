"""
Pertemuan 2 - Tugas 2
"""

class Bilangan:
    
    def __init__(self, angka):
        self.angka = angka
    
    def jenisBilangan(self):
        if self.angka == 0:
            print(f"{self.angka} adalah Nol")
        else:
            if self.angka % 2 == 0:
                print(f"{self.angka} adalah Genap")
            else:
                print(f"{self.angka} adalah Ganjil")

bil1 = Bilangan(1)
bil2 = Bilangan(0)
bil3 = Bilangan(-1)
bil4 = Bilangan(2)
bil5 = Bilangan(2)
bil1.jenisBilangan()
bil2.jenisBilangan()
bil3.jenisBilangan()
bil4.jenisBilangan()
bil5.jenisBilangan()