import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# weather_file.csv 파일을 읽어서
# 서울, 인천, 대전, 대구, 광주, 부산, 울산 지역의 기온, 습도를 선그래프로 출력
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

df = pd.read_csv('weather_select.csv', index_col='도시', encoding='euc-kr')

city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
print(city_df)

xdata = ['서울', '인천', '대전', '대구', '광주', '부산', '울산']
temp = city_df['기온']
hum = city_df['습도']
print(temp)
plt.figure(figsize=(10,6))
plt.plot(xdata, temp, label='기온')
plt.plot(xdata, hum, label='습도')
plt.legend()
plt.show()


# axes = city_df.plot(kind='line', title='지역별 기온 및 습도',
#                     figsize=(12,5), legend=True, fontsize=10)
# axes.set_xlabel('도시', fontsize=10)
# axes.set_ylabel('기온 및 습도', fontsize=10)
# axes.legend(['기온','습도'], fontsize=10)
# plt.show()


ax = city_df.plot(kind='bar', title='날씨', 
                    figsize=(12,7), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'], fontsize=12)
plt.show()