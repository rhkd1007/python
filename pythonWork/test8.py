import csv
import re


def opencsv(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)

    return output


total = opencsv('popSeoul2.csv')
print(type(total))
print(total[:5]) # 5개만 출력
for i in total[:5]:
    print(i)

print()
for i in total[:5]:
    for j in i:
        # print(i.index(j)) # 위치확인
        try:
            i[i.index(j)] = float(re.sub(',','',j))

        except:
            pass
print(total[:5])
print()
print(total)

test = [10,20,30,40,50]
# 50 의 위치값
print(test.index(50))

j = '1,468,246'
print(float(re.sub(',','',j)))
print(int(re.sub(',','',j)))
