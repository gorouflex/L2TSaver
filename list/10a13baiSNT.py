## Dang 2: So Nguyen To
n = int(input("Nhap so nguyen duong n: "))

## a) Kiem tra n co phai so nguyen to hay khong
d = 0
for i in range(1, n+1):
    if n % i == 0:
        d += 1
if d == 2:
    print(n, "la so nguyen to")
else:
    print(n, "khong la so nguyen to")

## b) Dua ra cac so nguyen to tu 2 den n
for i in range(2, n+1):
    d = 0
    for j in range(1, i+1):
        if i % j == 0:
            d += 1
    if d == 2:
        print(i, end=" ")

## c) Tinh tong/dem/trung binh cong cac so nguyen to tu 2 tu den n
print() ## Khong copy doan code nay
tong = 0
dem = 0
for i in range(2, n+1):
    d = 0
    for j in range(1, i+1):
        if i % j == 0:
            d += 1
    if d == 2:
        tong += i
        dem += 1
print("Tong cac so nguyen to tu 2 den n la:", tong)
print("Co", dem, "so nguyen to tu 2 den n")
if dem > 0:
    print("Trung binh cong cac so nguyen to tu 2 den n la:", tong/dem)

