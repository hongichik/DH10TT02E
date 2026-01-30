import random
while True:
    so_may = random.randint(1, 10)

    so_nguoi_dung = int(input("Nhập số dự đoán (1-10): "))

    if so_nguoi_dung > so_may:
        print("Lớn quá")
    elif so_nguoi_dung < so_may:
        print("Nhỏ quá")
    else:
        print("Chúc mừng!")
        break