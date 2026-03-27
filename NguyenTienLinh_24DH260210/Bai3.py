email = input("Hãy điền email: ")

def checkemail(email):
    if email.endswith("@gmail.com"):
        print("email hợp lệ")
    else:
        print("email ko hợp lệ")

checkemail(email)