import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt


dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='big9_db', charset='utf8', use_unicode=True)

select_busan = 'select * from forecast where city = "부산" order by tmef asc'
cur = conn.cursor()
cur.execute(select_busan)
busan_data = cur.fetchall()
print(busan_data)

low = []
high = []
xdata = []

for i in busan_data:
    low.append(int(i[4]))
    high.append(int(i[5]))
    # xdata.append(i[2])
    xdata.append(i[2].split('-')[2])

# 폰트 지정
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
# 그래프 크기
plt.figure(figsize=(10,6)) #크기

plt.plot(xdata, low, label='최저기온')
plt.plot(xdata, high, label='최고기온')
plt.title('2023/02/23 ~ 2023/03/02 부산 최고 및 최저 기온')
plt.legend()
plt.show()

#####################
select_data = 'select wf, count(*) from forecast where city="부산" group by wf'
cur.execute(select_data)
result_wf = cur.fetchall()
wfData = []
wfDataCount = []
for i in result_wf:
    wfData.append(i[0])
    wfDataCount.append(i[1])

plt.bar(wfData,wfDataCount,color='green')
plt.title('부산날씨 정보')
plt.show()

######################
plt.pie(wfDataCount, labels=wfData, autopct='%.1f%%')
plt.title('부산날씨 정보2')
plt.show()

#=========================================#
# # wf(구름많음, 흐림, 맑음)에 대한 막대 그래프와 원형 그래프 생성
# select_wf = 'select wf from forecast where city="부산"'
# cur.execute(select_wf)
# result_wf = cur.fetchall()
# # print(result_wf)

# wf_dic = {'구름많음' : 0, '흐림' : 0, '맑음' : 0}
# for i in result_wf:
#     if i[0] == '구름많음':
#         wf_dic['구름많음'] += 1
#     elif i[0] == '흐림':
#         wf_dic['흐림'] += 1
#     elif i[0] == '맑음':
#         wf_dic['맑음'] += 1
# print(wf_dic)

# # 막대 그래프 
# plt.bar(wf_dic.keys(), wf_dic.values())  
# plt.show()

# # 원형 그래프
# figure = plt.figure()
# axes = figure.add_subplot(111)
# axes.pie(wf_dic.values(), labels=wf_dic.keys(), autopct='%.1f%%')
# plt.show()

    