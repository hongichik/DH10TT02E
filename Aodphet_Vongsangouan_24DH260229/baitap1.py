import random

somay = random.randint(1, 100)

while True:
    sodoan = int(input("Nhập số bạn đoán (1-100): "))

    if sodoan > somay:
        print("Lớn quá")
    elif sodoan < somay:
        print("Nhỏ quá")
    else:
        print("Chúc mừng!")
        break