import jieba
txt = 'Python是最有意思的编程语言'
words = jieba.lcut(txt)
print(words)
