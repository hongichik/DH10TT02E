def nhap_sanpham():
    maSP = input("Nhập mã sản phẩm: ")
    tenSP = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá: "))
    return {"maSP": maSP, "tenSP": tenSP, "gia": gia}
def gia_trungbinh(ds_sp):
    if not ds_sp:
        return 0
    tong = sum(sp["gia"] for sp in ds_sp)
    return tong / len(ds_sp)
def loc_sanpham(ds_sp, gia=20000):
    return [sp for sp in ds_sp if sp["gia"] >= gia]
ds_sp = []
print("=== NHẬP THÔNG TIN 3 SẢN PHẨM ===")
for i in range(2):
    print(f"\nSản phẩm {i + 1}:")
    sp = nhap_sanpham()
    ds_sp.append(sp)

gtb = gia_trungbinh(ds_sp)
print(f"\nGiá trung bình: {gtb:.2f}")

print("\nDanh sách sản phẩm có giá >= 30000:")
ds_loc = loc_sanpham(ds_sp, gia=20000)
if ds_loc:
    for sp in ds_loc:
        print(f"  {sp['maSP']} - {sp['tenSP']}: {sp['gia']:.0f}")
else:
    print("  Không có sản phẩm nào.")