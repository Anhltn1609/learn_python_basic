#  Vì còn rất nhiều Trường Sinh Linh Giá khác nên Harry cần sự giúp đỡ của các bạn. Hãy giúp Harry tách list kia và in nó lên màn hình.
# Input:
# 	Dòng đầu tiên là một câu hoàn chỉnh
# 	Dòng thứ hai  là một list các chữ cái có trong câu.
# Output:
# 	In ra list sau khi đã tách.

# Mình thích harry nên mk sẽ làm bài này :v 

a = str(input("Nhâp vao một chuỗi: "))
b = list(input("list các chữ cái trong câu: "))
j = 0
c = []
start = 0
end = 0
for i in range(len(a)):
    if a[i] != b[i- j]:
        end = i-j
        c.append(b[start:end])
        start = i-j
        j += 1
c.append(b[start:])  
print("output: ", c)
# thử : dòng 1: anh yeu em nhieu vcl
#       dòng 2: anhyeuemnhieuvcl
#       output: [['a', 'n', 'h'], ['y', 'e', 'u'], ['e', 'm'], ['n', 'h', 'i', 'e', 'u'], ['v', 'c', 'l']]


