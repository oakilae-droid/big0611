from bs4 import BeautifulSoup

# strip() 매서드: 앞 뒤 공백 제거

html_doc = """
<span><br>                맨체스터 유나이티드     <br></sapan>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 공백이 가득한 상태
raw_text = soup.find('span').text
print(raw_text)
# 출력: "\n        맨체스터 유나이티디     \n"
