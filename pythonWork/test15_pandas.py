import pandas as pd

df = pd.read_csv('apt_201910.csv', encoding='cp949')
print(len(df))
print(type(df))
print(df.shape)
print(df.head())
print(df.tail())
print('-------------')
# 면적이 130보다 큰 거 출력
print(df.면적)
print('=============')
print(df[df.면적 > 200])
# 10개만 단지명 ,가격 출력
# txt = []
# for a, b in zip(df.단지명, df.가격):
#     txt.append([a,b])
# print(txt[:10])

print(df.loc[:10,['단지명','가격']])

# 단지명 ,가격, 면적 출력 단, 면적 130 보다 큰 거 출력
print(df.loc[df.면적>130,['단지명','가격','면적']]) # 같은 결과는 나오지만 선생님과 형식이 다름.
print(df.loc[:,['단지명','가격','면적']][df.면적 > 130])
