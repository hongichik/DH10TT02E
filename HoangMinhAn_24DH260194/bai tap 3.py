file_name = "minhan.csv"
def nhap_ds_sv():
    n = int(input("nhap vao so luong sinh vien: "))
    ds_sv = []
    for i in range(n):
        print("moi ban nhap sinh vien thu :",i , " !")
        maSV = input("nhap ma sinh vien: ")
        tenSv = input("nhap ten sinh vien : ")
        diem = float(input("nhap diem sinh vien: "))
        sv = {"maSV": maSV,"tenSV": tenSv,"diem": diem}
        ds_sv.append(sv)
    return ds_sv
def ghi_file(ds_sv, filename):
    with open(filename,"w") as file:
        file.write("Ma SV, Ten SV, Diem\n")
        for i in ds_sv:
            file.write(f"{i['maSV']},{i['tenSV']},{i['diem']}\n")
    return ds_sv
def doc_tt(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        ds_sv = []
        for line in lines[1:]:
            maSV, tenSV, diem = line.strip().split(",")
            sv = {"maSV": maSV, " tenSV" : tenSV , "diem": float(diem)}
            ds_sv.append(sv)
    return ds_sv
ds_sv =nhap_ds_sv()
ghi_file(ds_sv,file_name)
ds_sv = doc_tt(file_name)
print(ds_sv)