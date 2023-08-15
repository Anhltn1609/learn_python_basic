#  Dòng đầu là một số N:  5 <= N <= 100;
# 	N dòng tiếp theo, mỗi dòng là thông tin của một thí sinh bao gồm name và x:
# 	   		*Độ dài name:    3 <= len(name) <= 100
# 			*Giới hạn x: 1 <= x <= 10000
# 	Dòng cuối cùng là một số nguyên y thể hiện điểm sức mạnh của LONGMA:
# 			*Giới hạn: 1 <= y <= 10000
# 	Và LONGMA có tên là LONGMA =)))
# Output:
# 	YES: Nếu có thí sinh đánh bại được LONGMA 
# 	NO: Nếu không có ai mạnh bằng LONGMA
n = int(input("Nhập số lượng cao thủ: "))
l = []
for i in range(n) :
    l.append([str(input("Nhập tên cao thủ: ")).strip().upper(), int(input("Sức mạnh cao thủ: "))])

LONGMA = ["LONGMA",int(input("Nhap suc manh cua LONGMA: "))]

def logic(l,LONGMA):
    for i in range(len(l) - 1):
        if l[i][1] > LONGMA[1]:
            print("YES")
            return
        if l[i][1] == LONGMA[1] :
            if len(l[i][0]) > len(LONGMA[0]):
                print("YES")
                return
            else:
                print("NO")
                return 
    print("No")

logic(l,LONGMA)
        
