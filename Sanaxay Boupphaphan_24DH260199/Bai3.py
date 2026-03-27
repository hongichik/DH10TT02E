danh_sach_con_vat = ["chó", "mèo", "chim", "cá", "thỏ"]
print("Danh sách con vật:", danh_sach_con_vat)

# Thêm con vật vào cuối danh sách
con_vat_moi = input("Nhập tên con vật mới: ")
danh_sach_con_vat.append(con_vat_moi)
print("Danh sách con vật sau khi thêm:", danh_sach_con_vat)

# Thêm con vật vào vị trí index
index = int(input("Nhập vị trí index muốn thêm (0-{}): ".format(len(danh_sach_con_vat)-1)))
con_vat_moi = input("Nhập tên con vật mới: ")
danh_sach_con_vat.insert(index, con_vat_moi)
print("Danh sách con vật sau khi thêm theo index:", danh_sach_con_vat)

# Xóa con vật theo tên
con_vat_xoa = input("Nhập tên con vật muốn xóa: ")
if con_vat_xoa in danh_sach_con_vat:
    danh_sach_con_vat.remove(con_vat_xoa)
    print("Danh sách con vật sau khi xóa:", danh_sach_con_vat)
else:
    print("Con vật không có trong danh sách.")

# Sửa tên con vật
con_vat_cu = input("Nhập tên con vật muốn sửa: ")
if con_vat_cu in danh_sach_con_vat:
    con_vat_moi = input("Nhập tên con vật mới: ")
    index = danh_sach_con_vat.index(con_vat_cu)
    danh_sach_con_vat[index] = con_vat_moi
    print("Danh sách con vật sau khi sửa:", danh_sach_con_vat)
else:
    print("Con vật không có trong danh sách.")

# Số lượng con vật
print("Số lượng con vật trong danh sách:", len(danh_sach_con_vat))

# Xóa theo vị trí index
index_xoa = int(input("Nhập vị trí index muốn xóa (0-{}): ".format(len(danh_sach_con_vat)-1)))
danh_sach_con_vat.pop(index_xoa)
print("Danh sách con vật sau khi xóa theo index:", danh_sach_con_vat)