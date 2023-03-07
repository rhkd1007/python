# year  sales
# 2018 350
# 2019 400
# 2020 1050
# 2021 2000
# 2022 1000
import pandas as pd
data_dic = {
    'year' : [2018,2019,2020,2021,2022],
    'sales' : [350,400,1050,2000,1000]
}
print(data_dic)
print(type(data_dic))

df = pd.DataFrame(data_dic)
print(df)
print(type(df))
print('*'*20)

df2 = pd.DataFrame([[89.2, 92.5, 90.8],[92.8, 89.9, 95.2]],
index=['중간고사','기말고사'],
columns=['1반','2반','3반']
)
print(df2)

df3 = pd.DataFrame([[20231101,'Kim',90,80],[20231102,'Lee',80,70],[20231103,'Park',70,75],[20231104,'Han',50,60]
],
columns=['학번','이름','중간고사','기말고사'])
print(df3)
print(df3.sum())
print('*'*20)
#중간고사 합계
print('중간고사합계 : ',df3.중간고사.sum())
print('기말고사합계 : ',df3.기말고사.sum())
# 총점 추가
# print('총점 : ',(df3.중간고사.sum()+df3.기말고사.sum())) # 나의 방법
df3['총점'] = df3.중간고사 + df3.기말고사
print('*'*20)
print(df3)
print(df3.mean())
print('시험평균 : ', df3.총점.mean())
print('*'*20)
df4 = pd.DataFrame([[20231101,'Kim',90,80],[20231102,'Lee',80,70],[20231103,'Park',70,75],[20231104,'Han',50,60]
]
)
print(df4)
df4.columns=['학번','이름','중간고사','기말고사']
print(df4)
print(df4.tail())
print(df4.tail(2))
#파일 내보내기
df3.to_csv('exam01_pandas02.csv')
df33 = pd.read_csv('exam01_pandas02.csv')
print(df33)

df3.to_csv('exam01_pandas022.csv',header=False)
df333 = pd.read_csv('exam01_pandas022.csv', encoding='utf-8')
print(df333)