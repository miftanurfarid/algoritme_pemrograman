while True:
    try:
        x = int(input("masukkan angka: "))
        print(x)
    except ValueError:
        print("Masukkan angka saja, jangan yg lain")
