import random
while True:
    so_ngau_nhien = random.randint(1, 100)
    print(so_ngau_nhien)
    so_nhap =int(input(" nhập số dự đoán: "))

    if so_ngau_nhien > so_nhap:
        print("lớn quá")
    elif so_ngau_nhien < so_nhap:
        print("nhỏ quá")
    else:
        print("Đúng rồi")