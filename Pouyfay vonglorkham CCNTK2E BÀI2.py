import random

# Máy tính chọn số ngẫu nhiên từ 1 đến 100
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Nhập số bạn đoán (1-100): "))

    if guess > secret_number:
        print("Lớn quá")
    elif guess < secret_number:
        print("Nhỏ quá")
    else:
        print("Chúc mừng! Bạn đã đoán đúng ")
        break