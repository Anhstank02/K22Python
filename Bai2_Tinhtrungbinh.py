# Bai2_TinhTrungBinh.py

toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))

dtb = (toan + van) / 2

print("Điểm trung bình là:", dtb)

if dtb < 5:
    print("Xếp loại: Kém")
elif dtb < 7:
    print("Xếp loại: Trung bình")
elif dtb < 8:
    print("Xếp loại: Khá")
else:
    print("Xếp loại: Giỏi")
