
#append = them vao cuoi list
danhsacconvat=["cho","meo","chim","ca","tho"]
print("danh sac con vat:",danhsacconvat)
convatmoi= input("nhap ten con vat moi:")
danhsacconvat.append(convatmoi)
print("danh sach con vat sau khi them :",danhsacconvat)
# index = them vao vi tri index
index = int(input("nhap vi tri index muon them (0-{}):".format(len(danhsacconvat)-1)))
convatmoi=input("nhap ten con vat moi:")
danhsacconvat.insert(index,convatmoi)
print("danh sach con vat sau khi them theo index:",danhsacconvat)
# remove = xoa
convatxoa=input("nhap ten con vat can xoa :")
if convatxoa in danhsacconvat:
    danhsacconvat.remove(convatxoa)
    print("danh sach con vat sau khi xoa  :",danhsacconvat)
else:
    print("con vat khong co trong danh sach.")
#len = so luong trong danh sach
print("so luong con vat trong danh sach:",len(danhsacconvat))
#pop  = xoa theo gia tri key
index_xoa= int(input("nhap vi tri index muon xoa (0-{}):").format(len(danhsacconvat)-1))
danhsacconvat.pop(index_xoa)
print("danh sach sau khi xoa theo index:",danhsacconvat)