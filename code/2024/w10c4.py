def divide(x, y):
    try:
        hasil = x / y
    except ZeroDivisionError:
        print("penyebut tidak boleh NOL\n")
    except:
        print("Pokoknya salah\n")
    else:
        print(f"Hasilnya {x} / {y} adalah {hasil}\n")
    finally:
        print("bukanya masih lama\n")

while True:
    x = input("pembilang: ")
    y = input("penyebut: ")
    divide(x,y)