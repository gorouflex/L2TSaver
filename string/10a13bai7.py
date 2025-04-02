## Bai 7: VCT nhâp ho tên đầy đủ của người dùng, sau đó in thông báo tên và ho đêm của người đó.
s = input("Nhập ho tên đầy đủ của người dùng: ")
A = s.split()
ten = A[len(A)-1]
ho_dem = " ".join(A[0:len(A)-1])
print("Họ đệm của người đó là: ", ho_dem)
print("Tên của người đó là: ", ten)