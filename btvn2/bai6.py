# Input
# Một dòng gồm ba số a, b, n mỗi số các nhau một dấu cách( 1 <= a, b, n <= 10^6).
# Output
# 	Gồm 2 dòng
# 	Dòng đầu là số trường hợp có thể là số táo Đông đã đếm.
# 	Dòng hai list chứa các trường hợp đó, các phần tử trong list sắp xếp theo thứ tự
# tăng dần	

a,b,n = int(input("Nhap vao a: ")), int(input("Nhap vao b: ")), int(input("Nhap vao n: "))
c= []
sl =0
for i in range(a,a+n):
    if(i % n == 0):
        print(i)
        a = i 
for i in range(a,b,n):
    sl += 1
    c.append(i)

print("Số lượng các trường hợp: ", sl)
print("Dãy các số:", c)