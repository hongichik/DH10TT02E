import random
while True:
    sodoan = int (input("Nhap so doan (1-10): "))
    so = random.randint(1,10)
    if so == sodoan:
        print ("Chuc mung ban da doan dung!")
    elif sodoan == 99:
        print ("Ban da chon thoat cho choi.")
        break
    elif so > sodoan:
        print ("So ban doan nho hon so may chon.")
    else:
        print ("So ban doan lon hon so may chon.")

