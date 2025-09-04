while True:
    try:
        year = int(input("Nhập năm: ").strip())
        if year <= 0:
            print("Năm phải là số nguyên dương!")
            continue
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập năm là số nguyên hợp lệ!")

while True:
    try:
        month = int(input("Nhập tháng (1-12): ").strip())
        if month < 1 or month > 12:
            print("Tháng phải từ 1 đến 12!")
            continue
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập tháng là số nguyên hợp lệ!")

if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {month} năm {year} có 31 ngày.")
elif month in [4, 6, 9, 11]:
    print(f"Tháng {month} năm {year} có 30 ngày.")
elif month == 2:
    # Kiểm tra năm nhuận
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"Tháng 2 năm {year} có 29 ngày (năm nhuận).")
    else:
        print(f"Tháng 2 năm {year} có 28 ngày.")
else:
    print("Tháng không hợp lệ.")