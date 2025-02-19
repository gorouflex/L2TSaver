## Chuong trinh tim UCLN cua hai so a va b
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

m = a if a > b else b
i = 1
MAX = 1

while i <= m:
    if a % i == 0 and b % i == 0:
        MAX = i
    i += 1
print("UCLN:", MAX)

## Vi du:
# Nhap: a = 12, b = 18
# Xuat: UCLN: 6
