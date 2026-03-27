email = input("Hãy điền email: ")

def ktemail(email):
    if email.endswith("@gmail.com"):
        print("email hợp lệ")
    else:
        print("email ko hợp lệ")

ktemail(email)