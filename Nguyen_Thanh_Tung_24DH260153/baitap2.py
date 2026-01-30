import random

# Chọn số ngẫu nhiên từ 1 đến 100
so_bi_mat = random.randint(1, 100)
print("Tôi đã chọn một số từ 1 đến 100. Hãy đoán thử nhé!")

while True:
    # Người dùng nhập số dự đoán
    doan = int(input("Nhập số dự đoán của bạn: "))
    
    # So sánh và đưa ra gợi ý
    if doan > so_bi_mat:
        print("Lớn quá!")
        print("Số bí mật là:", so_bi_mat)
    elif doan < so_bi_mat:
        print("Nhỏ quá!")
        print("Số bí mật là:", so_bi_mat)
    elif doan < 1 or doan > 100:
        print("Số không hợp lệ, vui lòng nhập số từ 1 đến 100.")
    else:
        print("Chúc mừng!", so_bi_mat)
        break