from bs4 import BeautifulSoup

# shift+alt+a: 다중 문자열

html_doc = '''
<div id="content">
    안녕하세요. <span>홍길동</span>입니다.
    <p>반갑습니다!</p>
</div>
'''
# ctrl+.: 자동 임포트
soup = BeautifulSoup(html_doc, 'html.parser')
element = soup.find(id="content")

print(element.text)
# 출력:
# 안녕하세요. 홍길동입니다.
# 반갑습니다!