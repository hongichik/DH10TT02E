import random

while True:
    sodoan = int(input("Nhập số bạn đoán (1-10): "))
    so = random.randint(1, 10)
    if so == sodoan:
        print("Chúc mừng bạn đã đoán đúng!")
    elif sodoan == 99:
        print("Bạn đã chọn thoát trò chơi.")
        break
    elif so > sodoan:
        print("Số bạn đoán nhỏ hơn số máy chọn.")
    else:
        print("Số bạn đoán lớn hơn số máy chọn.")
