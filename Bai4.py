name = input("Hãy nhập tên của bạn: ")
print("Chào bạn,", name)
age_str = input("Hãy nhập tuổi của bạn: ")
print(f"Kiểu dữ liệu của 'age_str' là: {type(age_str)}")
while True:
    age_str = input("Hãy nhập tuổi của bạn:")
    print(f"Kiểu dữ liệu của 'age_str' là: {type(age_str)}")
    try:
        age_int = int(age_str)
        break
    except ValueError:
        print("Bạn phải nhập một số nguyên cho tuổi") 
print(f"Kiểu dữ liệu của 'age_int' là: {type(age_int)}")
age_after_10_years = age_int + 10
print(f"10 năm nữa, bạn sẽ {age_after_10_years} tuổi.")