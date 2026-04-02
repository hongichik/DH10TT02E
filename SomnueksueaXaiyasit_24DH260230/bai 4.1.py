hocsinh ={
    "name":"Pham hoai nam",
    "age":18,
    "class":"CNTT 1A",
}
print("Thong tin sinh vien:",hocsinh)

ds_hocsinh =[
    {"name":"Pham hoai nam","age":18,"class":"CNTT 1A" },
    {"name":"Nguye Van A","age":20,"class":"CNTT 1B" },
    {"name":"Nguye Van B","age":21,"class":"CNTT 1C" },
]

print("Danh sach hoc sinh :")
for hocsinh in ds_hocsinh:
    print(hocsinh)
#Vd ve sua thong tin hoc sinh thu 1
ds_hocsinh[0]["age"]=21
print("Danh sach hoc sinh sau khi sua :",ds_hocsinh[0])

hocsinh.pop("class")
print("Thong tin sinh vien sau khi xoa truong 'class':",hocsinh)
ds_hocsinh[0].pop("name")
print("Thong tin hoc sinh sau khi xoa truong 'name' ",ds_hocsinh[0])