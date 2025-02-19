## Chuong trinh tim BCNN cua hai so a va b su dung vong lap while

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
i = a if a < b else b 
MAX = 1 
while i > 0:
    if a % i == 0 and b % i == 0:
        MAX = i
    i = i - 1 
BCNN = a * b / MAX
print("BCNN:", BCNN)

## Vi du:
# Nhap: a = 12, b = 18
# Xuat: BCNN: 36
