hocsinh = {
    "name":"NguyenPhuongAnh",
    "age":20,
    "class": "CNTTK2E",
}
print("thông tin học sinh:", hocsinh)
ds_hoc_sinh = [
    {"name": "NguyenPhuongAnh","age":20,"class":"CNTTK2E"},
    {"name": "JeonJungKook", "age":28,"class":"CNTTK2E"},
    {"name": "KimTaeHyung", "age":30,"class":"CNTTK2E"},
]
print("Danh sách học sinh:")
for hoc_sinh in ds_hoc_sinh:
    print(hoc_sinh)
    # vd về sửa tt hs thứ nhất
    ds_hoc_sinh[0] ["age"] = 21
    print("Thong tin học sinh sau khi sửa:", ds_hoc_sinh[0])
    hoc_sinh.pop("class")
    print("Thông tin học sinh sau khi xóa trường 'class': ", hoc_sinh)
    ds_hoc_sinh[0].pop("name")
    print("Thong tin học sinh sau khi xoa truong 'name': ", ds_hoc_sinh[0])
