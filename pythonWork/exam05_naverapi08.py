import urllib.request
import json

clientId = '3JaFqqIF0UR8xoZ1oUi1'  # 자신의 ID
clientSecret = 'zeaQpeLKiQ'  # 자신의 Secret zeaQpeLKiQ


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", clientId)
    req.add_header("X-Naver-Client-Secret", clientSecret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')

    except:
        return None

#https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EC%9B%94%EB%93%9C%EC%BB%B5
def getNaverSearch(node, srcText, start, display):
    # url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)
    url = base+node+parameters

    responseDecode = getRequestUrl(url)
    # print(responseDecode)
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)  # loads() : JSON 문자열을 Python 객체로


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    bloggername = post['bloggername']
    link = post['link']
    postdate = post['postdate']
    bloggerlink = post['bloggerlink']
    jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                      'bloggername': bloggername, 'link': link, 'postdate': postdate, 'bloggerlink': bloggerlink})


node = 'blog'
srcText = input('검색어를 입력하세요 ')
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100)
# print(jsonResponse['total'])
total = jsonResponse['total']
while(jsonResponse != None) and (jsonResponse['display'] != 0):
    for post in jsonResponse['items']:
        cnt += 1
        getPostData(post, jsonResult, cnt)
    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 10)
print('전체 검색 : %d 건' % total)
print('가져온 데이터 : %d 건' % (cnt))

with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf-8-sig') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)
