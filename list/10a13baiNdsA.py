## Dang 1:
n = int(input("Nhap so nguyen n: ")) 
A = [] # Tao DS A rong
for i in range(1, n+1):
    so = int(input("Nhap so thu " + str(i) + ": "))
    A.append(so)

print("Danh sach so da nhap:", A) ## Khong can thiet neu de khong hoi in ra ds vua nhap
## Da hoan thanh 50% bai tu luan

## Cac dang yeu cau de co the ra:
## a) Dua ra so lon nhat, vi tri
max = A[0]
vitri = 0
for i in range(1, n):
    if A[i] > max:
        max = A[i]
        vitri = i + 1
print("So lon nhat", max, "o vi tri:", vitri)

## b) Dua ra so nho nhat, vi tri
min = A[0]
vitri = 0
for i in range(1, n):
    if A[i] < min:
        min = A[i]
        vitri = i + 1
print("So nho nhat:", min, "o vi tri:", vitri)

## c) Xoa cac so am trong DS
i = 0
while i < n:
    if A[i] < 0:
        del A[i]
        n = n - 1
    else:
        i = i + 1
print("Danh sach sau khi xoa cac so am:", A)

## d) Xoa cac phan tu chia het cho 5 trong DS
i = 0
while i < n:
    if A[i] % 5 == 0:
        del A[i]
        n = n - 1
    else:
        i = i + 1
print("Danh sach sau khi xoa cac phan tu chia het cho 5:", A)

## a,b,c,d la 50% con lai cua bai tu luan. Chuc may man!