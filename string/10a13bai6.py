## Bai 6: VCT nhâp một xâu kí tư có thể có nhiều dấu cách giữa các từ. Sau đó chỉnh sửa xâu kí tư đó sao cho giữa các từ chỉ có một dấu cách (dấu phẩy). In xâu kết quả ra màn hình.
s = input("Nhập một xâu kí tự có thể có nhiều dấu cách giữa các từ: ")
A = s.split()
for i in range(len(A)):
    print(A[i], end=" ")