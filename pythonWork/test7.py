import re
import csv

f = open('popSeoul.csv','r')
reader = csv.reader(f)


output = []
for i in reader:
    tmp = []
    for j in i:
        try:
            if re.search('\d',j):
                tmp.append(float(re.sub(',','',j))) # , 제거하고 출력
            else:
                tmp.append(j)

        except:
            pass

    output.append(tmp)

print(output)

a=100.56
print(round(a,1)) # 반올림

#외국인 비율이 5% 넘는 구만 출력 (구, 한국인, 외국인, 외국인비율(%))
result = [['구', '한국인', '외국인', '외국인비율(%)']]
for i in output:
    foreign=0
    try:
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        if foreign > 5:
            # print(i[0], i[1], i[2], foreign)
            result.append([i[0], i[1], i[2], foreign])   

    except:
        pass

####
print(result)