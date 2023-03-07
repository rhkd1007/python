import re
import codecs

f = codecs.open('friends101.txt','r',encoding='utf-8')
script101 = f.read()
print(script101[:100])

# Monica: 대사 3개 출력
lines = re.findall(r'Monica:.+',script101)
print(lines[:3])
print(type(lines))

# All: 대사 출력
all = re.findall(r'All:.+',script101)
print(all)
# All 의 마지막 대사
print(all[-1])
print(len(all))
print('=================')
patt = re.compile(r'[A-Z][a-z]+:') #패턴을 미리 정의 즉, 첫글자는 대문자"[A-Z]" 두번째부터는 소문자"[a-z]"여야하며 갯수"+"는 상관없고 끝은 ":"로 끝나야한다.
print(re.findall(patt, script101))

a = [1,2,3,4,5,2,2]
print(a)
print(set(a)) # 중복허용하지 않는다.
# 등장인물 출력 단, 중복 허용 안함
print(set(re.findall(patt,script101)))
y = set(re.findall(patt,script101))
print(type(y))
# y 를 리스트 lst 변환
lst = list(y)
print(type(lst))
print(lst)
print("*************")
# : 제거

character =[] # <class 'list'>
for i in lst:
    character += [i[:-1]]
print('character : ', character)

for i in lst:
    print(i)

character2 = [] # <class 'list'>
#sub 사용
for i in lst:
    charact = re.sub(':', '',i)
    print(charact, end=' ')
    character2.append(charact)
    # character2 += charact //영문자 1개씩 출력됨.
print()
print('character2 : ', character2)
##########################
print()
# 지문 출력
txt = re.findall(r'\([A-Za-z].+\.\)',script101)[:6] # 소괄호 안에서 점으로 끝나는걸 찾아라
print(">>txt : ", txt)
print(">>txt : ", len(txt))

txt1 = re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101)[:6] # 소괄호 안에서 점으로 끝나거나 소문자로 끝나는 걸 찾아라
print(">>txt : ", txt1)
print(">>txt : ", len(txt1))

txt1 = re.findall(r'\([A-Za-z].+?[a-z|\.]\)',script101)
print(">>txt : ", txt1)
print(">>txt : ", len(txt1))
#############################

# sub 이용해서 : 제거 하기
ch = 'Scene:'
ch = re.sub(':', '',ch)
print(ch)

#############################
a = '제 이메일 주소는 greate@naver.com'
a += ' 오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)
#메일주소만 출력
#a1 = re.findall(r'[a-z].+?\.[a-z]+',a) life@abc.co만 출력되는 오류가 있음
a1 = re.findall(r'[a-z]+@[a-z.]+',a)
print('메일주소 : ',a1)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# a로 시작하는 단어 출력
mm = []
for i in words:
    mm += re.findall(r'a[a-z]+',i)
print('~~~',mm)
print()

for i in words:
    m = re.search(r'a[a-z]+',i)
    if m:
        print(m.group())
# print('search : ', m)

for i in words:
    # m = re.match(r'a[a-z]+',i)
    m = re.match(r'a\D+',i) # \d 숫자 \D 숫자아닌
    if m:
        print('match : ',m.group())

# print('search : ', m)

