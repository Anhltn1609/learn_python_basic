# Input:
# 	Dòng đầu tiên là một số nguyên N: số lượng số mà Nasus có, 1 <= N <= 100
# 	Dòng thứ hai có N số nguyên, mỗi số cách nhau bởi một dấu cách. Giá trị mỗi số 
# 	nằm trong đoạn [1, 1000]
# Output: 
# 	Dòng đầu tiên là số lượng số thầy Ba thích trong các số Nasus có
# 	Dòng thứ hai là các số thầy Ba thích theo thứ tự tăng dần mà Nasus có


#  mk không thích thầy Ba nên mk sẽ chọn số thầy không thích
n = int(input("Nhap so luong cac so: "))
a = []
while len(a) != n:
    a = list(map(int, input("Nhập mảng các số: ").split()))

sl = 0
b = []
for i in range(len(a)):
    if(a[i]%2 == 1):
        sl += 1
        b.append(a[i])

print("Số lượng các số mà thầy Ba thích: ",sl )
print("Chuỗi các số thầy Ba thích: ", b)


