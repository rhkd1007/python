import requests

URL = 'https://www.naver.com/'
reponse = requests.get(URL)
print(reponse)
html_data = reponse.text
#print(html_data)
print(html_data.find('<h3 class="blind">'))
print(html_data.find('급'))
