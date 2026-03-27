import random
while True:
    sodoan= int(input("nhap sp doan :"))
    so = random.randint (1,10)
    if so == sodoan:
        print("ban da doan dung ")
    elif sodoan == 99:
        print("ban da thoat he thong")
        break
    elif so > sodoan:
        print("so doan lon hon so")
    elif so < sodoan:
        print("so doan nho hon so")
