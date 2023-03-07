import pandas as pd
import re

df = pd.read_csv('apt_201910.csv', encoding='cp949', thousands=',')

#면적이 200보다 큰 거 출력
print(df[df['면적']>200])
print()

#지역에 강릉이 들어간 자료만 출력
# print(df[df.시군구.str.find('강릉')>-1])

df_area = (df[df.시군구.str.find('강릉')>-1])
print(type(df_area))
print(df_area)
print()

# 지역이 강릉인 시군구, 가격, 면적 10행 출력
# print(df.loc[:10,['시군구','가격','면적']])
print(df_area.loc[:10,['시군구','가격','면적']])
print(df_area.loc[:10,('시군구','가격','면적')]) # 위와 같은 결과 출력
print()

# 면적이 130 넘는 아파트의 가격 출력
# print(df.loc[:,['가격']][df.면적 > 130])
print(df.가격[df.면적 > 130])
print()

#면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) & (df.가격 < 20000)])
print()

#면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) | (df.가격 < 20000)])
print()

dfAsc = df.sort_values(by='가격', ascending=False)
print(dfAsc.가격)

print('*'*20)
print(df.sort_values(by='가격', ascending=False).가격)

# df.loc[원하는 행 조건, 원하는 열의 조건]
# 9억원을 초가하는 가격으로 거래된 단지명(아파트), 가격 출력
print(df.loc[:,['단지명','가격']][df.가격>90000])

# 단가 = 가격 / 면적
# df.단가 = df.가격 / df.면적 #오류 df에 단가가 없음
# df.단가 df['단가'] 은 같지만 없는 컬럼을 생성할 때는 df['단가']만 가능
df['단가'] = df.가격 / df.면적
print(df.loc[:10,('시군구','면적','단가')])
print(df.단가)