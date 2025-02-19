n = int(input("Nhap so nguyen duong n: "))
S = 0
for i in range(1, n+1):
    if i%2==0:
        S = S+i
print("Ket qua: ",S)
