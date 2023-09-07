a = set(input("Nhập vào set thứ nhất :").split())
b = set(input("Nhập vào set thứ hai :").split())

intersection_s = a.intersection(b)
print("Sinh viên đăng ký đồng thời ở cả 2 bàn", intersection_s)

union_s = a.intersection(b)
print("Sinh viên đăng ký ở 2 bàn", union_s)

a_only_s = a.difference(b)
print("Sinh viên đăng ký ở bàn 1 mà không đăng ký ở bàn 2", a_only_s)

unique_s = a.symmetric_difference(b)
print("Sinh viên đăng ký ở duy nhất 1 bàn", unique_s)


