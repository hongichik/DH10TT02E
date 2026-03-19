import random
so_bi_mat = random.randint(1, 100)
so_lan_doan = 0
while True:
    try:
        doan = int(input("Nhập số bạn đoán: "))
        so_lan_doan += 1

        if doan < 1 or doan > 100:
            print("Số phải nằm trong khoảng 1 → 100 thôi nhé!")
            continue

        if doan > so_bi_mat:
            print("Lớn quá!")
        elif doan < so_bi_mat:
            print("Nhỏ quá!")
        else:
            print("Chúc mừng!")
            print(f"Bạn đã đoán đúng số {so_bi_mat} sau {so_lan_doan} lần đoán!")
            break

    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ nhé!")
