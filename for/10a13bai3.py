## Chuong trinh dem so luong uoc cua n
n = int(input("Nhap so nguyen duong n: "))
dem = 0
for i in range(1, n+1):
    if n % i == 0:
        dem = dem + 1
print("So luong cua uoc cua n:", dem)

## Vi du:
# Nhap: n = 6
# Xuat: So luong cua uoc cua n: 4 (1, 2, 3, 6)
