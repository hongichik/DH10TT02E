students = []

def add_student():
    sid = input("ID: ")
    name = input("Ten: ")
    age = input("Tuoi: ")
    students.append({"id": sid, "name": name, "age": age})

def show_students():
    for s in students:
        print(s["id"], s["name"], s["age"])

def find_student():
    sid = input("Nhap ID can tim: ")
    for s in students:
        if s["id"] == sid:
            print("Tim thay:", s)
            return
    print("Khong co sinh vien nay")

def delete_student():
    sid = input("Nhap ID can xoa: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Da xoa")
            return
    print("Khong tim thay sinh vien")

while True:
    print("\n1.Them  2.Xem  3.Tim  4.Xoa  5.Thoat")
    c = input("Chon: ")
    if c == "1": add_student()
    elif c == "2": show_students()
    elif c == "3": find_student()
    elif c == "4": delete_student()
    elif c == "5": break
    else: print("Sai lựa chọn")
