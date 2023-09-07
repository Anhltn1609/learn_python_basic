n = int(input("Nhập số lượng phần tử mảng: "))
a = []
for i in range(n):
    element = input("Nhập phẩn tử thứ {}: ".format(i+1))
    a.append(element)

b = tuple(a)
print("Các phần tử của tuple b: ")
print(b)

count = 0
for i in a:
    if i.isdigit():
        count += 1 

print("Có {} phần tử của mảng là số ".format(count))