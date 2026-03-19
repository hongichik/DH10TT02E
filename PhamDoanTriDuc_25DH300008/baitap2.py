import random
while True:
    n = int(input("nhập số bất kì từ 1 - 100: "))
    dapan = random.randint(1,100)
    if n > dapan:
        print("số lớn quá")
    elif n < dapan:
        print("số nhỏ quá")
    else:
        print("xin chúc mừng bạn đã đúng")
        break
    if input("nhập 1 để nhập lại \nnhập 0 để thoát\n") == "0":
        break
else:
    print("đã thoát")