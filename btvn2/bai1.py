import math


a =list(map(int, input("Nhập mảng có ít nhất 10 phần tử : ").split()))
# Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
dem = 0
x =int(input("Nhập x:"))
for i in a:
    if i == x :
        dem += 1
print("Số lần xuất hiện của {} là : {}".format(x,dem))
# Thay thế phần tử từ vị trí 2 -> 7 trong list thành [6, 9, 7, 0, 8, 0].
a[2:7] = [6,9,7,0,8,0]
print(a)
# Tìm số lớn nhất, và nhỏ nhất trong list.
maxx = max(a)
minn = min(a)
print("Số lớn nhất trong list: {}\nSố nhỏ nhất trong list: {}".format(maxx,minn ))

# Chèn x vào đầu danh sách
x= int(input("Nhap vao x : "))
a.insert(0,x)
print(a)

#  Nếu sắp xếp theo tăng dần thì in ra màn hình “TANG”, 
# còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIAM”,
# nếu không tăng không giảm thì in “NO”.
def kiem_tra_sap_xep(a):

    incre = True
    decre = True

    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            decre = False
        if a[i] > a[i+1]:
            incre = False
    
    if incre :
        print("Tang")
    elif decre:
        print("Giam", decre)
    else :
        print("No")

kiem_tra_sap_xep(a)

# Tạo một list mới có N phần tử. Các phần tử sẽ có vị trí từ 1 -> N. Với mỗi 
# phần tử ở vị trí i (1 <= i <= N) giá trị của nó là tổng i phần tử đầu tiên của list cũ.
def tao_list(a):
    x = 0
    l = []
    for i in range(len(a) - 1):
        x += a[i]
        l.append(x)
    return l

print("Mang mới: ", tao_list(a))

# Tạo một list mới [-1, 5, -76, 120, 234, 1000, -12, -7, 35]
#và sắp xếp nó theo thứ tự tăng dần của giá trị,
#và sắp xếp nó theo sự tăng dần của giá trị tuyệt đối.

b = [-1, 5, -76, 120, 234, 1000, -12, -7, 35]
b.sort()
print("Mảng b sau khi đã sắp xếp : ",b)

sorted_list = sorted(b, key=lambda x: abs(x))

print(sorted_list)