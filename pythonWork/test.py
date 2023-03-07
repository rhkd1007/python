print('Hello')
a = 0
print(a)
print(type(a))
b = 'Hello World'
print(b)
print(type(b))
c = "'안녕하세요'"
print(c)
d = "\'안녕하세요\'"
print(d)
print(b+c)
print(2*3)
print('2'*3)
print(c*3)
print('----------------')
print(b)
print(b[0])
print(b[-1])
e = '안녕하세요'
print(e[0:2]) #안녕
print(e[1:3]) #녕하
print(e[0:5:2]) #안하요
print(e[:]) #안녕하세요
print(e[2:]) #하세요
print(e[:3]) #안녕하
# list
l = list() #List l = new List() 자바는 이렇게
print(l, type(l))
lst = [1,2,3]
print(lst, type(lst))
l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(l, type(l))
print(l[0])
print(len(l))
# l 리스트의 마지막 값 출력
print('마지막 : ',l[len(l)-1]) #print('마지막 : ',l[12])
# l의 첫번째값을 99로 수정
l[0] = 99
print(l[0])
l[1] = [1,2,3]
print(l)
l[2] = '문자'
print(l)
l.append(999) #l(리스트)의 마지막 값
print(l)
l.remove(5)
print(l)

# tuple
t = tuple()
print(t, type(t))
t1 = (1,2,3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1+t1)
# t1의 첫번째값을 5로 수정
#t1[0] = 5  # 오류 발생 tuple은 수정이 안됨
print(t1)

# dic (자바에선 Map)
d = dict()
print(d ,type(d))
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d, type(d))
print(d['a'])
d['c'] = 33
print(d)
#print(d['d']) 오류발생
d1 = d.keys
print('d1 : ',d1)
d2 = d.items
print('d1 : ',d2)
############
d11 = d.keys()
print('key : ',d11, type(d11))
d22 = d.items()
print('items : ', d22, type(d22))
d33 = d.values()
print('values : ', d33, type(d33))

print("type list", type(list(d.keys())))

dset = set(d.keys())
print(dset, type(dset))

# 조건문 ==> *들여쓰기로 문장을 판단함*
a = 2
if(a == 1):
    print(1)
else:
    print("1아님")

if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    print(3)

print('---------')
#반복문
for i in [1,2,3]:
    print(i)

for i in (1,2,3):
    print(i)

for i in "Hello":
    print(i)

num = 5
while(num>0):
    print(num)
    num -= 1

print('--while---')
num=10
while(num > 0):
    if(num == 6):
        print('-----end----')
        break
    print(num, end = ' ')
    num -= 1

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')
print()
# 100 까지 수 중 7의 배수의 합계 출력
sum = 0
for i in range(100):
    if(i % 7 == 0):
        sum += i
        print(i, end=' ')
print("\nsum: " , sum)

# * * *
#print('* * *\n'*3) 하드코딩
for i in range(3):
    for j in range(3):
        print('*',end= ' ')
    print('')

d1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
value_max = max(d1.values())
print("max : ", value_max)

# key : a  value : 1
# max값을 가지는 키 값을 출력
for k , v in d1.items():
    print('key : ', k , 'values : ', v)
    if(v == value_max):
        print('key :' , k )
