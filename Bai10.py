while True:
    diem_str = input("Nhập điểm trung bình của học sinh: ").strip()
    try:
        diem = float(diem_str)
        if diem < 0 or diem > 10:
            print("Điểm phải nằm trong khoảng từ 0 đến 10!")
            continue
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ!")

if diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")