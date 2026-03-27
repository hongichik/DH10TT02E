danh_sach_con_vat = ["chó","mèo","chim","cá","thỏ"]
print("Danh sách con vật:", danh_sach_con_vat)
con_vat_moi= input("Nhập tên con vật mới: ")
danh_sach_con_vat.append(con_vat_moi)
print("Danh sách con vật sa khi thêm:", danh_sach_con_vat)
index = int(input("Nhập vị trí index muốn thêm(0-{}):"))-1
con_vat_moi = input("Nhập tên con vật mới:")
danh_sach_con_vat.insert(index, con_vat_moi)
print("Danh sách con vật sau khi thêm theo index: ", danh_sach_con_vat)
con_vat_xoa = input("Nhập tên con vật muốn xóa: ")
if con_vat_xoa in danh_sach_con_vat:
    danh_sach_con_vat.remove(con_vat_xoa)
    print("Danh sách con vật sau khi xóa: ", danh_sach_con_vat)
else:
    print("Con vật không có trong danh sách.")
con_vat_cu = input("Nhập tên con vật muốn sửa:")
if con_vat_cu in danh_sach_con_vat:
    con_vat_moi=input("Nhập tên con vật mới: ")
    index = danh_sach_con_vat.index(con_vat_cu)
    danh_sach_con_vat[index]=con_vat_moi
    print("Danh sách con vật sau khi sửa: ", danh_sach_con_vat)
else:
    print("Con vật không có trong danh sách")
    print("Số lượng con vật trong danh sách", len(danh_sach_con_vat))
    index_xoa= int(input("Nhập vị trí index muốn xóa(0-{}:"))-1
    danh_sach_con_vat.pop(index_xoa)
    print("Danh sách con vật sau khi xóa theo index",danh_sach_con_vat)