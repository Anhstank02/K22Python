#Vòng lặp xác định - câu lệnh for
danh_sach_mon_an = ["Cơm tấm", "Phở", "Bún chả", "Bánh mì", "Bún bò Huế"]

for mon_an in danh_sach_mon_an:
    print("Tôi thích ăn", mon_an)

#Tiếp tục( lặp qua một chuỗi string)
chuoi_ky_tu = "Python"

for ky_tu in chuoi_ky_tu:
    print(ky_tu)
    
#Vòng lặp for - với hàm range

for i in range(2, 11, 2):
    print(i)
    
#Câu lệnh break

danh_sach_so = [10, 25, 40, 55, 70]
so_can_tim = 40

for so in danh_sach_so:
    print(f"Dang kiem tra so: {so}")
    if so == so_can_tim:
        print("Da tim thay so can tim:", so)
        break

#Câu lệnh continue

for i in range(1,11):
    if i % 2 != 0:
        continue
    print(f"So chan: {i}")
    
#Vòng lặp không xác định - câu lệnh While

so_hien_tai = 1

while so_hien_tai <= 5:
    print("So hien tai la:", so_hien_tai)
    so_hien_tai += 1
    
mat_khau_chinh_sac = "python123"
mat_khau_nhap_vao = ""

while mat_khau_nhap_vao != mat_khau_chinh_sac:    
    mat_khau_nhap_vao = input("Nhap mat khau: ")
    if mat_khau_nhap_vao == mat_khau_chinh_sac:
        print("Dang nhap thanh cong!")
    else:
        print("Mat khau sai, vui long thu lai.")