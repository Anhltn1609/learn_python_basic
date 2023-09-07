string = str(input("Nhập vào một đoạn  văn"))

words = string.lower().split()
#tạo set để lưu trữ số lần xuất hienj của từng từ
word_counts = {}
#Đếm số lần xuất hiện của từ
for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

max_count = max(word_counts.values())

most_frequent_words = [(word, count) for word, count in word_counts.items() if count == max_count]
print(tuple(most_frequent_words))
