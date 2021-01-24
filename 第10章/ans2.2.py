import jieba
jieba.add_word('意大利面')
txt = '今天晚上我吃了意大利面'
words = jieba.lcut(txt)
print(words)
