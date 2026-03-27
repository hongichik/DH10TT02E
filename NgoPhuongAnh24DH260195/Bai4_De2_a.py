def nhap_sanpham():
    maSP = input("Nhap ma san pham: ")
    tenSP = input("Nhap ten san pham: ")
    gia = float(input("Nhap gia san pham: "))
    sanpham = {"maSP": maSP, "tenSP": tenSP, "gia": gia}
    return sanpham

a = nhap_sanpham()
def nhap_ds_sp():
    n = int(input("Nhap vao so luong SP: "))
    ds_sp = []
    for i in range(n):
        print("Moi ban nhap san pham thu ",i," !")
        ds_sp.append(nhap_ds_sp())
    return ds_sp

def gia_tb(ds):
    if len(ds) == 0:
        return 0
    tong = 0
    for i in ds:
        tong += i["gia"]
    return tong/len(ds)

def loc_sp(ds_sp, gia=20000):
    if len(ds_sp) == 0:
        print("Khong co sp khong doc duoc")
    ds_loc = []
    for i in ds_sp:
        if i["gia"] >= gia:
            ds_loc.append(i)
    return ds_loc
ds_dp = nhap_ds_sp
print(ds_dp)
print("Gia trung binh la: ")
print(gia_tb(ds_dp))
print("Gia san pham theo bo loc la: ")
print(loc_sp(ds_dp,30000))