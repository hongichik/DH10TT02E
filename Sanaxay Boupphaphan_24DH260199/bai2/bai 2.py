
name = "Thầy hồng."
# in hoa
print(name.upper())
#in thường
print(name.lower())
#xoá khoảng trắng ở đầu và cuối
print(name.strip())
kt = "432423asdas"
# kiểm tra xem đầu chuỗi có phải là chữ cần tìm hay không
print(kt.startswith("4"))
# kiểm tra xem cuối chuỗi có phải là chữ cần tìm hay không
print(kt.endswith("s"))
# đếm số lần xuất hiện trong chuỗi
print(kt.count("a"))
# tìm vị trí của chữ cần tìm
print(kt.find("s"))
# định giạng chuỗi
print("Tên tôi là {} và tôi {} tuổi.".format("Thầy Hồng", 30))
# đếm số lượng ký tự trong chuỗi
print(len(name))