file_name='baitap3.csv'
def nhap_ds_sv():
    n = int(input("Nhập vào số lượng SV: "))
    ds_sv = []
    for i in range(n):
        print("Mời bạn nhập sinh viên thứ ",i," !")
        maSV = input("Nhập vào mã SV: ")
        tenSV = input("Nhập vào tên SV:")
        diem = float(input("Nhập điểm SV: "))
        sv = {"maSV": maSV, "tenSV": tenSV, "diem": diem}
        ds_sv.append(sv)
    return ds_sv
def ghi_file(ds_sv, filename):
    with open(filename, "w") as file:
        file.write("Ma SV,Ten1 SV,diem\n")
        for i in ds_sv:
            file.write(f"{i['maSV']},{i['tenSV']},{i['diem']}\n")
def doc_tt(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        ds_sv = []
        for line in lines[1:]:
            maSV, tenSV, diem = line.strip().split(",")
            sv = {"maSV": maSV, "tenSV": tenSV, "diem": float(diem)}
            ds_sv.append(sv)
        return ds_sv
ds_sv= nhap_ds_sv()
ghi_file(ds_sv, file_name)
ds_sv = doc_tt(file_name)
print(ds_sv)

