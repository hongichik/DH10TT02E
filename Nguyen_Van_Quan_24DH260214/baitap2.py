import random

while True:
    so = random.randint(1,100)
    dudoan =int(input("nhap mot so bat ky: "))
    if so>dudoan:
        print("nho qua!")
        print(so)
    elif dudoan>100:
        print("Bạn đã thoát trò chơi!")
        break
    elif so<dudoan:
       print("Lon qua!")
       print(so)
    else:
      print("dung roi!")
      print("so may chon la: ",so)