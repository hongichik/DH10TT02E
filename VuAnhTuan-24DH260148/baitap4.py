# p1
# danh_sach_con_vat =["cho","meo","chim","ca","tho"]
# print("danh_sach_con_vat: ",danh_sach_con_vat)
# con_vat_ms=input("Nhap mot con vat: ")
# danh_sach_con_vat.append(con_vat_ms)
# print("danh_sach_con_vat sau khi them: ",danh_sach_con_vat)
# index=int(input("Nhap vi tri index muon them(0-{}):".format(len(danh_sach_con_vat)-1)))
# con_vat_ms=input("Nhap mot con vat ms: ")
# danh_sach_con_vat.insert(index,con_vat_ms)
# print("Danh sach con vat khi them theo index: ",danh_sach_con_vat)
# con_vat_xoa=input("Nhap mot con vat xoa: ")
# if con_vat_xoa in danh_sach_con_vat:
#     danh_sach_con_vat.remove(con_vat_xoa)
#     print("Danh sach con vat sau khi xoa: ",danh_sach_con_vat)
# else:
#     print("Con vat khong co trong danh sach.")
# con_vat_cu=input("Nhap mot con vat muon sua: ")
# if con_vat_cu in danh_sach_con_vat:
#     con_vat_ms=input("Nhap mot con vat : ")
#     index=danh_sach_con_vat.index(con_vat_cu)
#     danh_sach_con_vat[index]=con_vat_ms
#     print("danh sach con vat sau khi sua: ",danh_sach_con_vat)
# else:
#     print("Con vat khong co trong danh sach.")
# print("so lg con vat trong danh sach: ",len(danh_sach_con_vat))
# index_xoa=int(input("Nhap vi index muon xoa (0-{}): ".format(len(danh_sach_con_vat)-1)))
# danh_sach_con_vat.pop(index_xoa)
# print("Danh sach con vat sau khi xoa theo index: ",danh_sach_con_vat)
# p2
# hocsinh={
#     "name":"Nguyen Trung Hieu",
#     "age":20,
#     "class":"CNTTK2D",
# }
# print("thong tin hs: ",hocsinh)
# ds_hs=[
#     {"name":"Nguyen Trung Hieu","age":20,"class":"CNTTK2D"},
#     {"name":"Nguyen manh Gau", "age":20,"class":"CNTTK2D"},
#     {"name":"Tuyen Quang Minh Nhan","age":36,"class":"Hokage"},
#     {"name":"Vu Tri Ba Ta Tro","age":36,"class":"Jack"},
# ]
# print("da hoc sinh: ")
# for hocsinh in ds_hs:
#     print(hocsinh)
# ds_hs[0]["age"]=36
# print("thong tin hoc sinh:",ds_hs[0])
#
# hocsinh.pop("class")
# print("thong tin hoc sinh sau khi xoa truong 'class':",hocsinh)
# ds_hs[0].pop("name")
# print("Thong tin hs sau khi xoa truong",ds_hs[0])
# p3
# def nhap_sanpham():
#     masp=input("nhap ma san pham: ")
#     tensp=input("nhap ten sp pham: ")
#     gia=float(input("nhap gia pham: "))
#     sanpham={
#         "masp":masp,
#         "tensp":tensp,
#         "gia":gia
#
#     }
#     print("thon tin san pham: ",sanpham)
#     return sanpham
#
# def giaTb(ds_sp):
#     if len(ds_sp) == 0:
#         return 0
#     tong = sum(sp["gia"] for sp in ds_sp)
#     return tong / len(ds_sp)
# def loc_sanpham(ds_sp, gia=20000):
#     return [sp for sp in ds_sp if sp["gia"] >= gia]
# def main():
#     ds_sp = []
#     for i in range(3):
#         print(f"\nNhập sản phẩm thứ {i + 1}:")
#         sp = nhap_sanpham()
#         ds_sp.append(sp)
#     avg = giaTb(ds_sp)
#     print("\nGiá trung bình:", avg)
#     ds_loc = loc_sanpham(ds_sp,30000)
#     print("\nDanh sách sản phẩm có giá >= 30000:")
#     for sp in ds_loc:
#         print(sp)
# if __name__ == "__main__":
#     main()
def nhap_san_pham():
    maSP = input("Nhập vào mã SP: ")
    tenSP = input("Nhập vào tên SP: ")
    gia = float(input("Nhập giá SP: "))
    sanpham = {"maSP": maSP, "tenSP": tenSP, "gia": gia}
    return sanpham


def nhap_ds_sp():
    n = int(input("Nhập vào số lượng SP: "))
    ds_sp = []
    for i in range(n):
        print("Mời bạn nhập sản phẩm thứ ", i+1, "!")
        ds_sp.append(nhap_san_pham())
    return ds_sp


def gia_tb(ds):
    if len(ds) == 0:
        return 0
    tong = 0
    for i in ds:
        tong += i["gia"]
    return tong / len(ds)


def loc_sp(ds_sp, gia=20000):
    if len(ds_sp) == 0:
        print("Không có sp không lọc được")
    ds_loc = []
    for i in ds_sp:
        if i["gia"] >= gia:
            ds_loc.append(i)
    return ds_loc


ds_sp = nhap_ds_sp()
print(ds_sp)

print("giá trung bình là")
print(gia_tb(ds_sp))

print("giá sản phẩm theo bộ lọc là")
print(loc_sp(ds_sp, 30000))