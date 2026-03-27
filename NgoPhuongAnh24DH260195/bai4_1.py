hocsinh = {
    "name": "Chicken Little",
    "age": 20,
    "class": "CNTT 1A",
}

print("thong tin hoc sinh:", hocsinh)

ds_hoc_sinh = [
    {"name": "Chicken Little", "age":20, "class": "CNTT 1A"},
    {"name": "Nguyen Van A", "age": 19, "class": "CNTT 1B"},
    {"name": "Tran Thi B", "age": 21,"class": "CNTT 1C" },
]

print("Danh sach hoc sinh: ")
for hocsinh in ds_hoc_sinh:
    print(hocsinh)

ds_hoc_sinh[0]["age"] = 21
print("Thong tin hoc sinh sau khi sua: ", ds_hoc_sinh[0])
hocsinh.pop("class")
print("Thong tin hoc sinh sau khi xoa truong 'class': ", hocsinh)
ds_hoc_sinh[0].pop("name")
print("Thong tin hoc sinh sau khi xoa truong 'name': ", ds_hoc_sinh[0])
