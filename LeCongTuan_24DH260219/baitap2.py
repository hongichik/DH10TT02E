import random
so_can_doan = random.randint(1, 100)

print("=== TRÒ CHƠI ĐOÁN SỐ ===")
print("Máy đã chọn một số từ 1 đến 100")
while True:
    du_doan = int(input("Nhập số bạn đoán: "))
    if du_doan > so_can_doan:
        print("Lớn quá")
    elif du_doan < so_can_doan:
        print("Nhỏ quá")
    else:
        print("🎉 Chúc mừng! Bạn đã đoán đúng 🎉")
        break
