import random

so_bi_mat = random.randint(1, 100)

while True:
    du_doan = int(input("Nhập số bạn đoán: "))

    if du_doan > so_bi_mat:
        print("Lớn quá")
    elif du_doan < so_bi_mat:
        print("Nhỏ quá")
    else:
        print("Chúc mừng!")
        break