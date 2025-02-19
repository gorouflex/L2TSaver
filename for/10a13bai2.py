## Chuong trinh tinh tong cac so chan tu 1 den n
n = int(input("Nhap so nguyen duong n: "))
S = 0
for i in range(1, n+1):
    if i % 2 == 0:
        S = S + i
print("Ket qua:", S)

## Vi du:
# Nhap: n = 6
# Xuat: Ket qua: 12 (2 + 4 + 6 = 12)
