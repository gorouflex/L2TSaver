## Chuong trinh tinh tong lap phuong cac so tu 1 den n
n = int(input("Nhap so nguyen duong n: "))
S = 0
for i in range(1, n+1):
    S = S + i * i * i
print("KQ:", S)

## Vi du:
# Nhap: n = 3
# Xuat: KQ: 36 (1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36)
