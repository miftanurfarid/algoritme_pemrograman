import sys

try:
    f = open('initeks.txt')
    s = f.readline()
    i = int(s.strip())
except OSError:
    print("file ga ada nih")
except ValueError:
    print("harus angka dong")
except:
    print("salah!")
else:
    print(i)
    print('ga ada yg salah!')