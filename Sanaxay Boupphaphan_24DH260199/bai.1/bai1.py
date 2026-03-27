# 1. Xin chào
def xin_chao():
    print("Xin chào các bạn")


# 2. In số
def in_so(n):
    print(n)


# 3. Tổng
def tong(a, b):
    return a + b


# 4. Hiệu
def hieu(a, b):
    return a - b


# 5. Tích
def tich(a, b):
    return a * b


# 6. Thương
def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b


# 7. Bình phương
def binh_phuong(n):
    return n ** 2


# 8. Kiểm tra chẵn/lẻ
def kiem_tra_chan(n):
    if n % 2 == 0:
        return "Chẵn"
    else:
        return "Lẻ"


# 9. Số lớn hơn
def so_lon_hon(a, b):
    if a > b:
        return a
    else:
        return b


# 10. In từ 1 đến n
def in_tu_1_den_n(n):
    for i in range(1, n + 1):
        print(i)


# ---- Test thử ----
xin_chao()
in_so(5)
print("Tổng:", tong(3, 4))
print("Hiệu:", hieu(10, 3))
print("Tích:", tich(2, 5))
print("Chia:", chia(10, 2))
print("Bình phương:", binh_phuong(6))
print("Kiểm tra:", kiem_tra_chan(7))
print("Số lớn hơn:", so_lon_hon(8, 3))
in_tu_1_den_n(5)