file_name =""
def nhapdssv():
    n =int (input("Nhap vao so sinh vien:"))
    tt_sv =[]
    for i in range(n):
        print("Moi ban nhap sinh vien thu ",i,"!")
        hotenSV=input("Nhap ho ten SV:")
        gioitinh=input("Nhap gioi tinh SV:")
        d_tr=input("Nhap Diem trung binh SV:")
        ngaysinh =input("Nhap ngay sinh SV:")
        diachi =input("Nhap dia chi  SV:")
        hs={"Ho va Ten":hotenSV,"Gioi tinh":gioitinh,"Diem trung binh":d_tr,"Ngay Sinh":ngaysinh,"Dia chi":diachi}
        tt_sv.append(hs)
        return tt_sv
    def ghi_file(tt_sv,file_name):
        with open(file_name,"w") as file:
            file.write("Ho va Ten,Gioi tinh,Diem trung binh,Ngay Sinh,Dia Chi\n")
            for i in tt_sv:
                file.write((f"{i["Ho va ten"]},{i["Gioi tinh"]},{i["Diem trung binh"]},{i["Ngay sinh"]},{i["Dia chi"]}\n"))
                def doc_tt(filename):
                    with open(filename,"r") as file:
                        lines=file.readlines()
                        tt_sv=[]
                        for line in lines[1:]:
                           hotenSV,gioitinh,d_tr,diachi,ngaysinh=line.strip().split(",")
                    hs = {"Ho va Ten": hotenSV, "Gioi tinh": gioitinh, "Diem trung binh": d_tr, "Ngay Sinh": ngaysinh,
                          "Dia chi": diachi}
                    tt_sv.append(hs)
                    return tt_sv
                tt_sv=doc_tt(file_name)
                print(tt_sv)