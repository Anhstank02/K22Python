name = input("Hãy nhập tên của bạn: ").strip()
print(f"Chào bạn, {name}")

while True:
    age_str = input("Hãy nhập tuổi của bạn: ").strip()
    try:
        age_int = int(age_str)
        if age_int < 0 or age_int > 150:
            print("Tuổi phải nằm trong khoảng từ 0 đến 150!")
            continue
        break
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ cho tuổi!")

print(f"10 năm nữa, bạn sẽ {age_int + 10} tuổi.")
