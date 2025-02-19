n = int(input("Nhap so nguyen duong n: "))
S = 0
dem = 0
for i in range(1, n+1):
    if n%i==0:
        S = S + i
        dem = dem+1
tbc = S/dem
print("TBC:", tbc)
