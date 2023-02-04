#워드 클라우드
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
import cv2

names = ["어벤져스","어벤져스_에이지_오브 울트론 ","어벤져스_인피니티_워","어벤져스_앤드게임"]
dfs = []

#파일 불러오기
for name in names:
    dfs.append(pd.read_csv(f"./{name}.csv")) #불러온 파일들을 하나의 dfs라는 리스트에 저장
    
for df in dfs: #dfs에서 영화 데이터 하나씩 들고옴
    dic = {} #사전
    okt=Okt() #형태소 추출기

    for string in df['리뷰내용']:
        string=string.replace("\t","") #줄바꿈 표시를 없애주는 것
        string=string.replace("\n","") #줄바꿈 표시를 없애주는 것
        words = okt.nouns(string) #명사 추출
        for word in words: #추출된 명사를 하나씩 가져옴
            try: dic[word] += 1 #명사의 빈도수를 저장
            except: dic[word] = 1

    # wordclod 모듈 불러오기
    wc = WordCloud(font_path= r'C:/Users/김근영/삼각멘토링/NanumGothic.ttf', background_color='black',
                  width=512,height=512,max_words=300,max_font_size=250)

    #C:\Users\yangb\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf

    # wordclod 생성 
    wc.generate_from_frequencies(dic)
    plt.figure(figsize=(50,50)) #이미지 사이즈 지정
    plt.imshow(wc) #이미지의 부드럽기 정도
    plt.axis('off') #x y 축 숫자 제거
    plt.show() #이미지 보여주기
    plt.savefig(f"./data/image_wordcloud.png")#이미지 저장 형식