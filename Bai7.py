def nhap_so(thong_bao):
    """Hàm nhập số an toàn (float), chỉ chấp nhận số."""
    while True:
        try:
            so = float(input(thong_bao).strip())
            return so
        except ValueError:
            print(" Vui lòng nhập một số hợp lệ!")

# Nhập 2 số
num1 = nhap_so("Nhập số thứ nhất: ")
num2 = nhap_so("Nhập số thứ hai: ")

# In giá trị và kiểu dữ liệu
print(f"\nGiá trị num1 = {num1}, kiểu dữ liệu: {type(num1)}")
print(f"Giá trị num2 = {num2}, kiểu dữ liệu: {type(num2)}")

# Thực hiện các phép toán cơ bản
print("\n--- Kết quả các phép toán ---")
print(f"Tổng: {num1} + {num2} = {num1 + num2}")
print(f"Hiệu: {num1} - {num2} = {num1 - num2}")
print(f"Tích: {num1} * {num2} = {num1 * num2}")

# Chia
if num2 != 0:
    print(f"Thương: {num1} / {num2} = {round(num1 / num2, 2)}")  # làm tròn 2 chữ số
else:
    print(" Không thể chia cho 0!")

# Chia lấy dư (chỉ khi là số nguyên và số chia khác 0)
if num2 != 0 and num1.is_integer() and num2.is_integer():
    print(f"Chia lấy dư: {int(num1)} % {int(num2)} = {int(num1) % int(num2)}")
elif num2 == 0:
    print(" Không thể chia lấy dư cho 0!")
else:
    print(" Không thể chia lấy dư vì ít nhất một số không phải số nguyên.")
