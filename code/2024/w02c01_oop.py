"""
Pertemuan 2 - Tugas 1
"""

from math import sqrt


class Segitiga:

    def __init__(self, sisi1, sisi2) -> None:
        self.sisi1 = sisi1
        self.sisi2 = sisi2

    def panjangMiring(self):
        return sqrt(self.sisi1**2 + self.sisi2**2)


segitiga1 = Segitiga(2,3)
segitiga2 = Segitiga(6,9)