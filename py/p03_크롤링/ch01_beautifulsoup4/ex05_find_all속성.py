# 두 번째 웹 크롤링 실습
# 테이블과 목록 정보 크롤링
# https://ai-dev.tistory.com/2

# 테이블 정보 크롤링
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://ai-dev.tistory.com/2'
html = urlopen(url)
# print(html.read())

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 방법1 - <table> 태그 이용
table_tag = soup.find_all('table')
# print(table_tag)
# print(table_tag[0])

table_tag01 = table_tag[0].find_all('td')
# print(table_tag01)

for idx, ele in enumerate(table_tag01):
    print(idx, ele.text)
'''
0 상품
1 색상
2 가격
3 셔츠1
4 빨강
5 20000
6 셔츠2
7 파랑
8 19000
9 셔츠3
10 초록
11 18000
12 바지1
13 검정
14 50000
15 바지2
16 파랑
17 51000
'''

com_list = soup.find_all('ul')
# print(com_list)

"""
    list-style-type: disk | circle | square;
"""
# com_list01 = soup.find_all('ul', {'속성': '값'})
com_list01 = soup.find_all('ul', {'style': 'list-style-type: disk;'})
# print(com_list01)

com_list02 = com_list01[0].find_all('li')
for idx, ele in enumerate(com_list02):
    print(idx, ele.text)
