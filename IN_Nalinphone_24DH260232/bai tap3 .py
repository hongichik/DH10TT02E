hocsinh = {
    "name": "Phạm Hoài Nam",
    "age": 20,
    "class": "CNTT 1A",
}
print("Thông tin học sinh:", hocsinh)

ds_hoc_sinh = [
    {"name": "Phạm Hoài Nam", "age": 20, "class": "CNTT 1A"},
    {"name": "Nguyễn Văn A", "age": 19, "class": "CNTT 1B"},
    {"name": "Trần Thị B", "age": 21, "class": "CNTT 1C"},
]
print("Danh sách học sinh:")
for hoc_sinh in ds_hoc_sinh:
    print(hoc_sinh)

# Ví dụ sửa thông tin học sinh thứ 1
ds_hoc_sinh[0]["age"] = 21
print("Thông tin học sinh sau khi sửa:", ds_hoc_sinh[0])

hocsinh.pop("class")
print("Thông tin học sinh sau khi xóa trường 'class':", hocsinh)

ds_hoc_sinh[0].pop("name")
print("Thông tin học sinh sau khi xóa trường 'name':", ds_hoc_sinh[0])
