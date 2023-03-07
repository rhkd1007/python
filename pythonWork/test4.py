import re  # 문자의 정규화를 위한 re
text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7])
print(text.find('문'))  # 있으면 위치값 리턴
print(text.find('파'))  # 없으면 -1 리턴
print(text.index('문'))  # index 있으면 위치값 리턴
# print(text.index('파')) # index 없으면 오류 발생

text1 = "   <title>지금은 문자열 연습입니다.</title>   "
text2 = ";"
print(text1.strip()+text2)  # strip 공백제거
print(text1.lstrip()+text2)  # lstrip 왼쪽공 백제거
print(text1.rstrip()+text2)  # rstrip 오른쪽 공백제거
print(text.replace('<title>', "<div>"))
print(text.replace('<title>', " "))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>', text3)  # .* 문자가 여러개 들어간다라는 뜻(.은 문자를 뜻함)
print(body)
body = body.group()
print(body)
print("---------------")

# [0-9] 0부터9까지 [a-z] a부터 z까지
# *(0이상)  +(1이상)  ?(0이상 1이하) //정규표현식
# ab*c : 예시) ac abc abbc abbbc abbbbc

text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
print(text4)
# <title>지금은 문자열 연습</title> 출력
body = re.search('<title.*/title>',text4)
body = body.group()
print(body) # <title>지금은 문자열 연습</title>

print('-----------------')
print(re.search('<.+>',body).group())
print('=================')
print(re.search('<.+?>',body).group())
print('#################')
# <title>지금은 문자열 연습</title>
body = re.sub('<.+?>','',body) # re.sub(a,b,c) c에서 a를 b로 대치하는 것
print(body)

example = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2023년입니다.'
txt = re.findall(r'\d.+년',example) #r뒤에는 문자로 간주해달라는 뜻 /d는 숫자라는 뜻 즉, 숫자가 오고 그뒤에 무엇이 올진 모르지만 같이 출력하고 년으로 끝나는 것을 출력하라는 뜻.
print(txt) # ['91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2023년']
txt1 = re.findall(r'\d.+?년',example)
print(txt1) # ['91년', '97년', '2023년']
