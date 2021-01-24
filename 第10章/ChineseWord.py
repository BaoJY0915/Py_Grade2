import jieba
from wordcloud import WordCloud
txt = '宋小萍啊宋小萍，迟早被包驾驭操死，狠狠操,操的你妈的都不认识了'
words = jieba.lcut(txt)
print(words)
newtxt = ' '.join(words) 
word = WordCloud(font_path = 'msyh.ttc').generate(newtxt)
word.to_file('sxpword.png')
