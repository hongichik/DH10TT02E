file_name = "filebt5.csv"


def nhap_ds_sv():
    n=int(input("moi nhap so lg sv: "))
    ds_sv = []
    for i in range(n):
        print("Nhap vao sv thu", i + 1, "!")
        gt = input("gioi tinh: ")
        tensv = input("ten sv: ")
        diem = float(input("diem tb: "))
        nssv = input("ngay sinh: ")
        dcsv = input("dia chi: ")

        sv = {
            "tensv": tensv,
            "gioi tinh": gt,
            "diemtb": diem,
            "ngay sinh": nssv,
            "dia chi": dcsv,
        }
        ds_sv.append(sv)
    return ds_sv


def ghi_file(ds_sv, filename):
    with open(filename, "w") as file:
        file.write("ten sv,gioi tinh,diemtb,ngay sinh,dia chi\n")
        for sv in ds_sv:
            file.write(
                f"{sv['tensv']},{sv['gioi tinh']},{sv['diemtb']},{sv['ngay sinh']},{sv['dia chi']}\n"
            )


def doc_tt(filename):
    with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                tensv, gt, diem, nssv, dcsv = line.split(",")
                sv = {
                    "tensv": tensv,
                    "gioi tinh": gt,
                    "diemtb": float(diem),
                    "ngay sinh": nssv,
                    "dia chi": dcsv,
                }
                ds_sv.append(sv)


    return ds_sv

ds_sv = nhap_ds_sv()
ghi_file(ds_sv, file_name)
ds_doc = doc_tt(file_name)
print(ds_doc)
