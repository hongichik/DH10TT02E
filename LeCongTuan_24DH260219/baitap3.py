email = input("Hãy điền email: ")

def Kt(email):
    if email.endswith("@gmail.com"):
        print("email hợp lệ")
    else:
        print("email ko hợp lệ")

Kt(email)