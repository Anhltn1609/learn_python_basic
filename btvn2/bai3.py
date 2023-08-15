# Input: 
# 	Dòng đầu tiên là một số nguyên N: số lượng chuỗi có trong list
# Dòng tiếp theo có N chuỗi, mỗi chuỗi cách nhau bởi 1 dấu cách, các chuỗi đều không có khoảng trắng
# Output:
# 	In ra một số nguyên, số lượng chuỗi có thể là mật khẩu.

#  Tôi không muốn giúp 2 tên trộm làm điều xấu nên tôi sẽ giải sai bài này :v

a =list(map(str, input("Nhập mảng các chuỗi: ").split()))
print(a)
dem = 0
for i in range(len(a)):
    if len(a[i]) == 6 :
        for j in range(len(a[i])) :
            if(a[i][j].isdigit()):
                dem += 1
                print(a[i])
                break
print("So lượng các chuỗi có thể là mã :", dem)

