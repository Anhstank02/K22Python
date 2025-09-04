while True:
    num_str = input("Nhập một số nguyên: ").strip()
    if num_str.lstrip('-').isdigit():
        num = int(num_str)
        break
    else:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

if num % 2 == 0:
    print("Đây là số chẵn.")
else:
    print("Đây là số lẻ.")