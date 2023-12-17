def diskonBarang(harga_lama):
    diskon = harga_lama * 20 / 100
    harga_baru = harga_lama - diskon

    return harga_baru


while True:
    harga = int(input('masukkan harga awal: '))

    if harga > 50000:
        print(f'harga awal = {harga}')
        hargaDiskon = diskonBarang(harga)
        print(f'harga setelah diskon = {hargaDiskon}')
        break
    else:
        continue

