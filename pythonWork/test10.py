import csv
import usecsv
import re

# apt_201910.csv 파일을 usecsv 에 있는 함수 사용하여 3개 출력
ap = usecsv.opencsv('apt_201910.csv')
apt = usecsv.switchcsv(ap)

print(apt[:3])
# apt_201910.csv 총 개수
print(len(apt))
# 시군구 단지명 가격 ==> 6개 출력
for i in apt[:6]:
    print(i[0],i[4],i[-4])

print()

# 강원도에 120 m2 이상 3억 이하 검색하기 시군구 단지명 가격 출력
new_List = [['시군구','단지명','가격']]
for i in apt:
    try:
        if i[5] >= 120 and i[8] <= 30000 and re.match('강원',i[0]):        
            #print([i[0],i[4],i[-4]])
            new_List.append([i[0],i[4],i[-4]])
    except:
        pass

print(new_List[:4])

# 파일로 출력
# with open("apt11.csv","w",newline='') as f:
#     a = csv.writer(f, delimiter=",")
#     a.writerows(new_List)

####################
# 첫번째 행에서 컴퓨터, 노트북, 테블릿
# 두번째 행에 100,80,60
# 리스트 형태로 표현
test_list=[['컴퓨터', '노트북', '테블릿'],[100,80,60]]

# test.csv 파일로 내보내기
with open("test.csv","w",newline='') as f:
    a = csv.writer(f)
    a.writerows(test_list)