## Chuong trinh tinh tong S = 1 + 1/2 + 1/3 + ... + 1/n
n = int(input("Nhap so nguyen duong n: "))
S = 0
for i in range(1, n+1):
    S = S + 1 / i
print("KQ:", S)

## Vi du:
# Nhap: n = 3
# Xuat: KQ: 1.8333 (1 + 1/2 + 1/3 = 1.8333)
