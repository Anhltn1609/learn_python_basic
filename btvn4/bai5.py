n = int(input("Nhập số lượng phần tử của set"))
s = set()
for i in range(n):
    element = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    s.add(element)

print(s)
fl = False
for  i in s: 
    if i == 11:
        fl = True
        break

if fl == False :
    s.add(11)
    print("set s sau khi thêm 11: {}".format(s) )
else:
    print("Set đã có số 11 rồi!")

a = []
for i in s:
    for j in s:
        if i + j == 11 :
            a.append(i,j) 

