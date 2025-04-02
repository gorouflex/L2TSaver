## Bai 5: Viết CT nhập 2 số nguyên dương cách nhau bởi dấu cách. Sau đó in ra màn hình UCLN của 2 số này
s = input("Nhập 2 số nguyên dương cách nhau bởi dấu cách: ")
A = s.split()
m = int(A[0])
n = int(A[1])
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print("UCLN của 2 số này là: ", m)
