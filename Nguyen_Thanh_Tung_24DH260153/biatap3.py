# # def Doctendoituong(ten="chua co ten"):
# #     if ten == "hong":
# #         print("day la thay giao cua toi")
# #     else:
# #         print("ban sinh vien ten:" + ten)
# # # Doctendoituong("hong")
# # def hieu(a,b):
# #     print("hieu:",a-b)
# # hieu(5,3)
# def xinchao():
#     for i in range(5):
#      print("xinchao lan : ",i + 1)
# xinchao()
email = input("nhap gmail: ")

print(email.endswith("@gmail.com"))

while True:
    if email.endswith("@gmail.com"):
        print("hop le")
    else:
        print("ko hop le")
    break


