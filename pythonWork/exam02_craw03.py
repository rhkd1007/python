import requests

r = requests.get("https://api.aoikujira.com/time/get.php")
txt = r.text # 텍스트 형식으로 데이터 추출
print(txt)

bin = r.content # 바이너리 형식으로 데이터 추출
print(bin)
