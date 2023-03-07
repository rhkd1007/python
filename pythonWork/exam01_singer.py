import re
import csv
import pandas as pd
# singer2.csv 읽어 [이름 조회수] 300000 넘는 거 출력
f = open('singer2.csv','r')
reader = csv.reader(f)
singer = []
for i in reader:
    singer.append(i)

print(singer)
print()
for i in singer:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',','',j))
        except:
            pass
print(singer)
print()
txt=[['이름', '조회수']]
for i in singer:
    try:
        if i[-1] >= 300000:
            txt.append([i[1],i[-1]])
    except:
        pass

print(txt)
print()

# 파일로 내보내기 youtube30.csv
with open("youtube30.csv","w",newline='') as f:
    a = csv.writer(f)
    a.writerows(txt)


# pandas read_csv
# 유튜브 조회수가 300000 넘는 거 출력

df = pd.read_csv('singer2.csv', encoding="cp949", thousands=',')
# print(df)
# print(df['유튜브 조회수'])
# print(df.유튜브 조회수) # 띄어쓰기(공백)가 존재함으로 사용 불가
print(df[df['유튜브 조회수']>300000])
