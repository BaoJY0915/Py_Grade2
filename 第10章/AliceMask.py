import jieba
from scipy.misc import imread
mask = imread('AliceMask.png')
from wordcloud import WordCloud
f = open('红楼梦.txt','r',encoding = 'utf-8')
txt = f.read()
words = jieba.lcut(txt)
##print(words)
newtxt = ' '.join(words) 
word = WordCloud(background_color = 'white',\
                 width = 800,\
                 height = 600,\
                 max_words = 200,\
                 max_font_size = 80,\
                 mask = mask,\
                 font_path = 'msyh.ttc',\
                 ).generate(newtxt)
word.to_file('hlm.png')
