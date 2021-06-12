
def read_file(filename):
    data = []
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            data.append(line)
            count += 1
            if count % 100000 == 0:
                print(len(data))
        return data
    print(f'檔案讀取完畢，共有{len(data)}筆資料。')


def average_len(data):
    sum_review = 0
    for review in data:
        sum_review += len(review)
    avg_review = sum_review / len(data)
    print(f'每筆留言平均長度：{avg_review}')


def less_then(data):
    words_list = []
    for words in data:
        if len(words) < 100:
            words_list.append(len(words))
    #List Comprehension 清單快寫法
    # words_list = [len(words) for words in data if len(words) < 100]
    print(f'留言長度小於100的總共有{len(words_list)}筆。')


def good(data):
    good_list = []
    for good in data:
        if 'good' in good:
            good_list.append(good)
    #List Comprehension 清單快寫法
    # good_list = [good for good in data if 'good' in good]
    print(f'留言裡有提到good的總共有{len(good_list)}筆。')


def total_words(data):
    word_count = {}
    for d in data:  # d：每一筆留言
        words = d.split()
        for word in words:  # word：每一筆留言中的每一個字
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1  # 表示第一次出現就在新增至字典，value = 1
    return word_count


def more_then(word_count):
    for word in word_count:
        if word_count[word] >= 1000000:
            print(f'「{word}」出現超過一百萬次！')


def looking_for(word_count):
    print('開始本查詢功能，輸入「q」可以離開。')
    while True:
        word = input('您想查什麼字呢：')
        if word == 'q':
            break
        if word in word_count:
            print(f'「{word}」出現{word_count[word]}次')
        else:
            print(f'「{word}」沒有出現過哦！')


def main():
    filename = 'reviews.txt'
    data = read_file(filename)
    average_len(data)
    less_then(data)
    word_count = total_words(data)
    more_then(word_count)
    looking_for(word_count)


main()
print('感謝您使用本查詢功能！')
