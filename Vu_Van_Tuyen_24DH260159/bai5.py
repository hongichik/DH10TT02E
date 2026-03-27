danh_sac_con_vat = ["chó", "mèo", "chim", "cá", "thỏ"]

print("Danh sách con vật:", danh_sac_con_vat)

# Thêm vào cuối danh sách
con_vat_moi = input("Nhập tên con vật mới: ")
danh_sac_con_vat.append(con_vat_moi)
print("Danh sách sau khi thêm:", danh_sac_con_vat)

# Thêm theo vị trí index
index = int(input("Nhập vị trí index muốn thêm (0-{}): ".format(len(danh_sac_con_vat))))
con_vat_moi = input("Nhập tên con vật mới: ")
danh_sac_con_vat.insert(index, con_vat_moi)
print("Danh sách sau khi thêm theo index:", danh_sac_con_vat)

# Xóa theo tên
con_vat_xoa = input("Nhập tên con vật muốn xóa: ")
if con_vat_xoa in danh_sac_con_vat:
    danh_sac_con_vat.remove(con_vat_xoa)
    print("Danh sách sau khi xóa:", danh_sac_con_vat)
else:
    print("Con vật không có trong danh sách.")

# Sửa tên con vật
con_vat_cu = input("Nhập tên con vật muốn sửa: ")
if con_vat_cu in danh_sac_con_vat:
    con_vat_moi = input("Nhập tên mới: ")
    index = danh_sac_con_vat.index(con_vat_cu)
    danh_sac_con_vat[index] = con_vat_moi
    print("Danh sách sau khi sửa:", danh_sac_con_vat)
else:
    print("Con vật không có trong danh sách.")

# Số lượng phần tử
print("Số lượng con vật:", len(danh_sac_con_vat))

# Xóa theo index
index_xoa = int(input("Nhập vị trí index muốn xóa (0-{}): ".format(len(danh_sac_con_vat)-1)))
if 0 <= index_xoa < len(danh_sac_con_vat):
    danh_sac_con_vat.pop(index_xoa)
    print("Danh sách sau khi xóa theo index:", danh_sac_con_vat)
else:
    print("Index không hợp lệ.")

