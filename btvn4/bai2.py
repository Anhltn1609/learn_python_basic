import itertools

n = int(input("Nhập vào một số nguyên dương :"))
s = set(map(int,input("Nhập vào set gồm {} phần tử: ".format(n)).split()))
num = float(input("Nhập vào một số :"))


largest_subset = set()
largest_sum = 0

for i in range(1, n+1):
    subsets = itertools.combinations(s, i)
    # tất cả các set con của s 
    for subset in subsets:
        subset_sum = sum(subset)
        if subset_sum <= num and subset_sum >= largest_sum :
            largest_sum = subset_sum
            largest_subset = set(subset)
        
print ("Tập con lớn nhất là : ", largest_subset)