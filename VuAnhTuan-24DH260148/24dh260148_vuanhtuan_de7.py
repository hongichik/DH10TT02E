def nhap_sach():
    ma_sach = input("Nhap ma sach: ")
    ten_sach = input("Nhap ten sach: ")
    gia = float(input("Nhap gia sach: "))
    ttsach = {
        "ma": ma_sach,
        "ten": ten_sach,
        "gia": gia,
    }
    return ttsach


def nhap_ds_sach():
    n = int(input("Nhap so luong sach: "))
    sach = []
    for i in range(n):
        print("Moi ban nhap sach thu", i + 1)
        sach.append(nhap_sach())
    return sach


def tong_gia_sach(sach):
    if len(sach) == 0:
        return 0
    return sum(ttsach["gia"] for ttsach in sach)


def loc_sach(sach, gia_max=200000):
    if len(sach) == 0:
        return []

    ds_loc = []
    for ttsach in sach:
        if ttsach["gia"] <= 100000:
            ds_loc.append(ttsach)
    return ds_loc

sach = nhap_ds_sach()
print("Danh sach sach:")
print(sach)

print("Tong gia sach la:")
print(tong_gia_sach(sach))

print("Danh sach sach co gia nho hon 100000:")
print(loc_sach(sach))
