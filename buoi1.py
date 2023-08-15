#biến , đối tượng

# đối tượng có 3 đặc điểm : type, id, value
a = 1
print(id(a)) 
print(type(a))  

# kiểu dữ liệu
s = 'abc'
t = 'gsf'
print(s,t)

#list lưu trữ nhiều items trong 1 biến duy nhất
#tuple tương tự với list nhưng items đc sắp xếp theo thứ tự và ko thể thay đổi
# dictionary là tập hợp được sắp xếp theo thứ tự * có thể thay đổi không cho phép trùng lặp
# được lưu theo cặp key - value
# dict =
# print(*object, sep = '', end = '\n', file = sys.stdout, flush = false) 
# flush là xóa bộ nhớ đệm mặc định là false
# file là địa chỉ xuất đối tượng ra file
# with open("output.txt", "w") as f
#   print(s, file = f)
# 
print(s)
with open("E:\\bai1.txt", "w") as f:
    print(s, file = f)

#print()
a =1 
b =2
print('{} +{} = {} '.format(a,b,a+b))
print(f' { a} +  { b} =  { a+b}')

print( not 1)

# toán tử khai khác 
# in và not int

print(type([3,4]))

# is và not is

a = 5
b = 5
print(b is a)

q = [2,3,4]
w = [2,3,4]

print(q is w)

# các kiểu dữ liệu thay đổi đc (mutable)
# list, dict, set, bytearray
# ko thể thay đổi đc (immutable)
# int float, string, tuple, range, frozenset

a = 341341342941394
b = 341341342941394
print(id(a), id(b))
b = 34134134294139
print(id(b))


if(4 & (not 0)):
    print("true")
else :
    print("false")

a = [ 'a', 'b', 'c', 'd' ]

# for i in a :
#     print(i, end="  ")

 
# for idx, val in enumerate(a):
#     print(idx, val)



b = [1,2,3,4,4]

for idx, val in enumerate(b) :
    print(idx, val)

print("****")
i=0
# while i < len(b):
#     if b[i] %2 == 0:
#         print(b[i], end = "  ")
#     i+=1

while i < b.count():
    if b[i] %2 == 0:
        print()