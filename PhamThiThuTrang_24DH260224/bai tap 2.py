hocsinh = {
    "name": "Phạm Thị Thu Trang",
    "age": 20,
    "class": "CNTTK2E",
}
print("Thông tin học sinh:", hocsinh)

ds_hoc_sinh = [
    {"name": "Phạm Thị Thu Trang", "age": 20, "class": "CNTTK2E"},
    {"name": "Nguyễn Văn A", "age": 20, "class": "CNTTK2E"},
    {"name": "Trần Thị B", "age": 20, "class": "CNTTK2E"},
]
print("Danh sách học sinh:")
for hoc_sinh in ds_hoc_sinh:
    print(hoc_sinh)
ds_hoc_sinh[0]["age"] = 21
print("Thông tin học sinh sau khi sửa:", ds_hoc_sinh[0])

hoc_sinh.pop("class")
print("Thông tin học sinh sau khi xóa trường 'class':", hoc_sinh)
ds_hoc_sinh[0].pop("name")
print("Thông tin học sinh sau khi xóa trường 'name':", ds_hoc_sinh[0])

