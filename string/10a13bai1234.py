## VCT nhập nhiều số nguyên từ bàn phím (một xâu), các số cách nhau bởi dấu cách
s = input("Nhập các số nguyên cách nhau bởi dấu cách: ")
## Bai 1: (Dùng lênh split() để tách thành danh sách)
A = s.split()
print(A)
## Bai 2 & 3: Khi nhập xong thông báo số lượng các số đã nhập & Chuyển các phần tử danh sách này thành số và in ra màn hình.
n = len(A)
print("Số lượng số nguyên đã nhập là: ", n)
DS = []
for i in range(len(A)):
    DS.append(int(A[i]))
for i in range(len(DS)):
    print(DS[i], end=" ")
print() # Không copy đoạn này!
## Bai 4: Sau đó in ra màn hình tổng các số đã nhập.
print("Tổng các số đã nhập là: ", sum(DS))