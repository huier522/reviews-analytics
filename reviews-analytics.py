data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
print(f'檔案讀取完畢，共有{len(data)}筆資料。')

sum_review = 0
for review in data:
    sum_review += len(review)
avg_review = sum_review / len(data)
print(f'每筆留言平均長度：{avg_review}')
