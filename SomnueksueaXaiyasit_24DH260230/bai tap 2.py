import random

while True:
 sd = int (input("nhap so vao 1-10 :"))
 so = random.randint(1, 10)
 if sd == so:
     print("dung roi")
     print("so random la:",so)
 elif sd ==99 :
     print("nhap so lai")
     break
 elif sd > so:
     print("so ban nhap lon hon so ramdom")
     print("so random la:",so)
 else:
     print("so ban nhap nho hon so ramdom")
     print("so random la:",so)
