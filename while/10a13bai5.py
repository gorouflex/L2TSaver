## Chuong trinh tim UCLN cua hai so a va b
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
m = 0
if a>b:
    m = a
else:
    m = b
MAX = 0
for i in range(1, m+1):
    if a%i==0 and b%i==0:
        MAX = i
print("UCLN:", MAX)

## Vi du:
# Nhap: a = 12, b = 18
# Xuat: UCLN: 6
