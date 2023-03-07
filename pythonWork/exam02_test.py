import re
import pandas as pd


# 1 . 1~10가지의 합 출력
sum=0
for i in range(1,11):
    sum+=i
print('sum : ', sum)
# 2 . 구구단 출력(2단 ~ 9단)
for i in range(2,10):
    print(i, "단")
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    print()

# 3 . 년도만 출력
exam = "저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2023년입니다."
res = re.findall(r'\d.+?년', exam)
print(res)

# 4 . .으로 구분하여 문장 출력
d = 'I have a dog. I am not a girl. Yoi ar not alone. I am happy'
ret1 = re.split('\.',d)
print(ret1)
ret2 = d.split('.')
print(ret2)


# dtxt = re.findall(r'.+?\.',d) #I am happy가 안나옴.
# print(dtxt)


txt = "Phoebe: Just, 'cause, I don't want her to go through what I went through with Carl- oh!"
txt += "Monica: Okay, everybody relax."
txt += "This is not even a date."
txt += "It's just two people going out to dinner and- not having sex."
txt += "Chandler: Sounds like a date to me."
txt += "Chandler: Alright, so I'm back in high school, I'm standing in the middle of the cafeteria, and I realize I am totally naked."
# 등장인물 출력
txt1 = re.findall(r'[A-Z][a-z]+:', txt)
print(txt1)

# 등장인물 중복 제거하고 출력
txt2 = set(txt1)
print(txt2)

6_1. # 문자열에서 무작위로 5개 문자 추출하여 새로운 변수 pw에 하나씩 병합
import random
pw = str()
chars = '한글우수'
for _ in range(5):
    pw = pw + random.choice(chars)
print(pw)

6. # animal 리스트에서 새가 저장되어 있는 위치(인덱스만) 저장하는 리스트
bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']
# for i in animals:
#     if re.match('새',i):
#         bird_pos.append(i.index)
# print(bird_pos)      

for i in range(len(animals)):
    if animals[i]=='새':
        bird_pos.append(i)

print(bird_pos)

# 4부터 animals끝까지 중에 첫번째 만나는 새의 위치값
# bird_pos.append(animals.index('새',4,len(animals)))

for i, animal in enumerate(animals):
    print(i, ":", animal)
    if animal == '새':
        bird_pos.append(i)

print(bird_pos)

7. # mylist 에서 짝수만 출력
mylist = [3,5,4,9,2,8,2,1]
new_list = []
for i in mylist:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

# 리스트 함축 : for 문과 if 조건식을 함축적으로 결합한 형식
# [i for i in 리스트명 if 조건식 ]

new_list2 = [i for i in mylist if i%2 == 0 ]
print('>>>',new_list2)
print('>>> type', type(new_list2))