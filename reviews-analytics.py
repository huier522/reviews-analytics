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

# words_list = []
# for words in data:
#     if len(words) < 100:
#         words_list.append(len(words))
#List Comprehonsion 清單快寫法
words_list = [len(words) for words in data if len(words) < 100]
print(f'留言長度小於100的總共有{len(words_list)}筆。')

# good_list = []
# for good in data:
#     if 'good' in good:
#         good_list.append(good)
#List Comprehonsion 清單快寫法
good_list = [good for good in data if 'good' in good]
print(f'留言裡有提到good的總共有{len(good_list)}筆。')
bad_list = [bad for bad in data if 'bad' in bad]
print(f'留言裡有提到bad的總共有{len(bad_list)}筆。')
