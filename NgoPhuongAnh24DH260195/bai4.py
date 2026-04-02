danh_sach_con_vat = ["cho", "meo", "chim", "ca", "tho"]
print("Danh sach con vat:", danh_sach_con_vat)
con_vat_moi = input("Nhap ten con vat moi: ")
danh_sach_con_vat.append(con_vat_moi)
print("Danh sach con vat sau khi them:", danh_sach_con_vat)
index = int(input("Nhap vao vi tri index muon them (0-{}):".format(len(danh_sach_con_vat)-1)))
con_vat_moi = input("Nhap ten con vat moi: ")
danh_sach_con_vat.insert(index, con_vat_moi)
con_vat_xoa = input("Nhap ten con vat muon xoa")
if con_vat_xoa in danh_sach_con_vat:
    danh_sach_con_vat.remove(con_vat_xoa)
    print("danh sach con vat sau khi xoa:", danh_sach_con_vat)
else:
    print("Con vat khong co trong danh sach.")
con_vat_cu = input("Nhap ten con vat muon sua:")
if con_vat_cu in danh_sach_con_vat:
    con_vat_moi = input("Nhap ten con vat moi")
    index = danh_sach_con_vat.index(con_vat_cu)
    danh_sach_con_vat[index] = con_vat_moi
    print("Danh sach con vat sau khi sua:", danh_sach_con_vat)
else:
    print("Con vat khong co trong danh sach")

print("So luong con vat trong danh sach:", len(danh_sach_con_vat))
index_xoa = int(input("Nhap vi tri index muon xoa (0-{}): ".format(len(danh_sach_con_vat)-1)))
danh_sach_con_vat.pop(index_xoa)
print("Danh sach con vat sau khi xoa theo index: ", danh_sach_con_vat)
