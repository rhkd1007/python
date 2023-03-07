import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# sales.csv파일로 저장
df = pd.DataFrame([[500, 450, 520, 610], [690, 700, 820, 900],
                   [1100, 1030, 1200, 1380], [1500, 1650, 1700, 1850],
                   [1990, 2020, 2300, 2420], [1020, 1600, 2200, 2500]],
                  index=[2015, 2016, 2017, 2018, 2019, 2020],
                  columns=['1분기', '2분기', '3분기', '4분기']
                  )
# print(df)
df.to_csv('sales.csv', header=False, encoding='euc-kr')
########################
df = df.transpose() # 행 열 전환
df.plot()
plt.show()
################
y1 = [500, 450, 520, 610]
y2 = [690, 700, 820, 900]
y3 = [1100, 1030, 1200, 1380]
y4 = [1500, 1650, 1700, 1850]
y5 = [1990, 2020, 2300, 2420]
y6 = [1020, 1600, 2200, 2500]
df1 = pd.DataFrame([y1,y2,y3,y4,y5,y6],index=[2015, 2016, 2017, 2018, 2019, 2020],
                  columns=['1분기', '2분기', '3분기', '4분기'])
df1.to_csv('sales1.csv', header=True ,encoding='euc-kr')


x=range(len(y1))
xLabel = ['first','second','third','fourth']
plt.plot(x, y1, color='b')
plt.plot(x, y2, color='orange')
plt.plot(x, y3, color='green')
plt.plot(x, y4, color='red')
plt.plot(x, y5, color='purple')
plt.plot(x, y6, color='brown')

plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.xticks(x, xLabel, fontsize=10)
# plt.yticks()
plt.legend(['2015', '2016', '2017', '2018', '2019', '2020'], loc='upper left')
plt.show()


# df2 = pd.read_csv('sales1.csv',encoding='euc-kr')

# font_name = mpl.font_manager.FontProperties(
#     fname='c:/Windows/fonts/malgun.ttf').get_name()
# mpl.rc('font', family=font_name)

# axes = df2.plot(kind='line', title='분기 보고서', figsize=(12,7), legend=True, fontsize=12)
# axes.set_xlabel('분기',fontsize=12)
# axes.set_ylabel('판매',fontsize=12)
# axes.legend(['년도'],fontsize=12)
# plt.show()
