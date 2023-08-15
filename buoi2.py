string1 = 'Hello'
string1 = "Hello"
string1 = """Hello"""
string1 = '''Hello
    cái này có thể xuống dòng'''

# escape sequence
a = "\bbb"
# dùng chuỗi trần để vô hiệu hóa escape sequence 
a = r"\bbbb"
# không thể thay đổi môt phần của string 
s = "abcs"
# s[4] = 3 => lỗi 
# s[start:end:step]

s = "HIT+Python"
# print(s[0:6])
# print(s[0:-4])
# print(s[-10:-4])
# print(s[0:4])
# print(s[1::2])
# print(s[-1:1:-1])
# print(s[10:0:-2])
# vị trí step dương vị trí bắt đầu bên trái
# nếu step âm đi từ đuôi lên 

# nhập chuỗi s từ bạn phím in các ký tự ở vị trí chia hết cho 3
# print(s[1:len(s):3] + "  " + s[-3 ::-3])

# lower 
# upper
# split
# strip
# join
# len
# find 
# replace
# b = s.lower()
# s.split('  ')
# s.join(s)

# a = input()
# b = a.split()
# c = len(b)
# print(c)

# comperhension
# l = [ i for i in range(10) if i %2 == 0 ]
# k = [i for i in input().split()]
# print(k)

l = [ 1,2,3,4,5]
l[:2] = [10]

# Nếu gán list b = list a thì khi a thay đổi b cũng thay đổi 
a =list(map(int, input().split()))
print(a)
# for i in a :
#     a[i] = int()
# a.sort()
# print(a)
# b = list(input())
# b.sort(reverse=True)
# print(b)
# a.extend(b)
# print(a)

# 1 2 5 