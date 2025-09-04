#Câu lệnh if
tuoi = 20
if tuoi >= 18:
    print("Ban du tuoi de lai xe")

#Câu lệnh if..else
diem_so = 7.5
if diem_so >= 5.0:
    print("Ban da qua mon")
else:
    print("Ban phai hoc lai.")
    
#Câu lệnh if...elif...else
diem_trung_binh = 8.5
if diem_trung_binh >= 9.0:
    print("Hoc luc: Xuat sac")
elif diem_trung_binh >= 8.0:
    print("Hoc luc: Gioi")
elif diem_trung_binh >= 7.0:
    print("Hoc luc: Kha")
elif diem_trung_binh >= 5.0:
    print("Hoc luc: Trung binh")
else:
    print("Hoc luc: Yeu")