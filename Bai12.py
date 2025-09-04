while True:
    try:
        a = float(input("Nhập hệ số a: ").strip())
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập số thực hợp lệ cho a!")

while True:
    try:
        b = float(input("Nhập hệ số b: ").strip())
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập số thực hợp lệ cho b!")

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    # Định dạng nghiệm: tối đa 6 chữ số thập phân, bỏ .0 nếu là số nguyên
    if x == int(x):
        x = int(x)
    else:
        x = round(x, 6)
    print(f"Nghiệm duy nhất x = {x}")