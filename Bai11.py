while True:
    kwh_str = input("Nhập số kWh điện đã tiêu thụ: ").strip()
    try:
        kwh_float = float(kwh_str)
        if kwh_float < 0:
            print("Số kWh phải là số không âm!")
            continue
        kwh = int(kwh_float)  # Lấy phần nguyên để tính tiền
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ!")

tien = 0
if kwh <= 50:
    tien = kwh * 1678
elif kwh <= 100:
    tien = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    tien = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
elif kwh <= 300:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
elif kwh <= 400:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
else:
    tien = (50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 +
            100 * 2834 + (kwh - 400) * 2927)

print(f"Số kWh được tính tiền: {kwh}")
print(f"Tổng tiền phải trả: {tien:,} VNĐ")