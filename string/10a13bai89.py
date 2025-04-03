## VCT nhập số tự nhiên n, rồi nhập họ tên của n học sinh.
n = int(input("Nhập số tự nhiên n: "))
TEN = []
HO = []
for i in range(n):
    s = input("Nhập họ tên của học sinh thứ " + str(i+1) + ": ")
    A = s.split()
    ten = A[len(A)-1]
    ho_dem = " ".join(A[0:len(A)-1])
    TEN.append(ten)
    HO.append(ho_dem)

## Bai 8: In ra danh sách tên học sinh theo hai cột, cột 1 là tên, cột 2 là họ đệm.
print("Tên         Họ đệm")
for i in range(len(TEN)):
    kc = " " * (10 - len(TEN[i]))
    print(TEN[i], kc, HO[i])

## Bai 9: Sau đó yêu cầu nhâp một tên và thông báo số bạn có cùng tên đó trong lớp.
s = input("Nhập tên cần tìm: ")
dem = 0
for i in range(len(TEN)):
    if TEN[i] == s:
        dem = dem + 1
print("Số bạn có cùng tên đó trong lớp là: ", dem)
