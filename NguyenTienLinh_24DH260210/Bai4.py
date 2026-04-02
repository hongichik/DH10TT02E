chuoikt = input("Nhập chuỗi kí tự: ")
def demkitua(chuoikt):
    print("Số lượng kí tự a: ",chuoikt.count("a"))
def demkitu(chuoikt):
    return len(chuoikt.replace(" ", ""))
print("Số ký tự (không tính khoảng trắng):", demkitu(chuoikt))

demkitua(chuoikt)
demkitu(chuoikt)