data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
print(f'檔案讀取完畢，共有{len(data)}筆資料。')