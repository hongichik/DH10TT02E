
def nhap_sanpham():
    maSP = input("Nhập mã sản phẩm: ")
    tenSP = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))

    return {
        "maSP": maSP,
        "tenSP": tenSP,
        "gia": gia
    }

def gia_trungbinh(ds_sp):
    if len(ds_sp) == 0:
        return 0

    tong = sum(sp["gia"] for sp in ds_sp)
    return tong / len(ds_sp)


def loc_sanpham(ds_sp, gia=20000):
    return [sp for sp in ds_sp if sp["gia"] >= gia]


def main():
    ds_sp = []

    print("Nhập thông tin 3 sản phẩm:")
    for i in range(3):
        print(f"\nSản phẩm {i + 1}:")
        ds_sp.append(nhap_sanpham())


    tb = gia_trungbinh(ds_sp)
    print("\nGiá trung bình:", tb)


    ds_loc = loc_sanpham(ds_sp, 30000)

    print("\nDanh sách sản phẩm có giá >= 30000:")
    for sp in ds_loc:
        print(sp)



main()




