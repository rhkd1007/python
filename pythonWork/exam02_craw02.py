from bs4 import BeautifulSoup
import re

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa</li>
    </ul>
"""
# https://example.com/fuga
# https://example.com/foo

soup = BeautifulSoup(html, 'html.parser')
print(soup)
lis = soup.find_all(href=re.compile(r'^https://')) # ^시작 기호
print(lis)
for e in lis:
    print(e.attrs["href"])