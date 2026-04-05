email = "exemple@gmail.com"
def kiemtra(email):
 if "com" in email:
     print("email hop ly")
 else:
     print("email khong hop ly")
     kiemtra(email)