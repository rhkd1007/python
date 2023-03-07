def seperate():
    a = int(input("수 입력"))
    if a % 2 == 0:
        print("짝수")
    else:
        print("홀수")

#두 수를 더하는 함수


def addReturn(a,b):
    return a+b


seperate()
print(addReturn(3,5)) #8
ret = addReturn(13,15)
print(ret)
