from urllib.request import urlopen
from bs4 import BeautifulSoup

# 주식 데이터 웹 크롤링과 데이터베이스 다루기
# 주식 사이트에 접속하기
# https://comp.fnguide.com


# 주식 데이터 크롤링
# 기본 정보 웹 크롤링

url = "http://wcomp.fnguide.com/?c_id=AA&menu_type=01&cmp_cd=005930"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 1. 날짜
date1 = soup.find('span', {'class':'date'})
print(date1.text)

# 날짜의 형식 변경
# [2026/08/14] -> 2026-08-14
date2 = date1.text
# replace(이전텍스트, 새텍스트)
date = date2.replace('[', '').replace(']', '').replace('/','-')
print(date)


# 2. 종목 이름 - find_all, find 차이 => []
corp_name1 = soup.find_all('h1', {'id':'giName'})
# print(corp_name1)
# [<h1 id="giName">삼성전자</h1>]
# corp_name = corp_name1[0].text
# print(corp_name)
corp_name1 = soup.find('h1', {'id':'giName'})
# print(corp_name1)
# <h1 id="giName">삼성전자</h1>
corp_name = corp_name1.text
print(corp_name)

# 3. 종목 코드
# code = soup.find_all('h2')
'''
[<h2>005930</h2>, <h2>12월 결산</h2>, <h2><strong>주가추이,</strong> 내부자거래<span class="blind" id="svdMainTopChart1">1년</span></h2>, <h2><strong>외국인 지분율,</strong> 시가총액<span class="blind" id="svdMainTopChart2">1년</span></h2>, <h2>
<strong>상대수익률</strong><span class="blind" id="svdMainTopChart3">1Y</span>
</h2>, <h2>시세현황</h2>, <h2>실적이슈</h2>, <h2>운용사별 보유 현황</h2>, <h2>주주현황</h2>, <h2>주주구분 현황</h2>, <h2>투자의견 컨센서스</h2>, <h2>투자의견 및 목표주가</h2>, <h2>투자의견 분포</h2>, <h2>Business Summary</h2>, <h2>업종 비교</h2>, <h2>Band Chart</h2>, <h2>PER Band</h2>, <h2>PBR Band</h2>, <h2>주가 및 수급현황</h2>, <h2>대차잔고비중</h2>, <h2>차입공매도비중</h2>, <h2>Financial Highlight</h2>]
'''
code = soup.find_all('h2')[0].text
print(code)
# 005930


# 4. 주가: 방법1
stock_price1 = soup.find_all('td', {'class':'cle r'})
stock_price = int(stock_price1[5].text.replace(',', ''))
print(stock_price)


# 4. 주가: 방법2
stock_price1 = soup.find("tr", {"class":"rwf"})
# 1. r 클래스를 가진 td 태그를 먼저 찾습니다.
td_tag = stock_price1.find("td", {"class": "r"})

# 2. td 태그 바로 아래에 있는 첫 번째 텍스트 노드를 추출하고, 공백과 ',', '/'를 제거합니다.
stock_price1 = td_tag.find(string=True).replace('/', '').replace(',', '').strip()
stock_price = int(stock_price1)
print(stock_price)  # 출력: 279500


# 5. 외국인 보유 비중
fgn_own_ratio1 = soup.find('span', {'id':'forignRatioStr'})
print(fgn_own_ratio1)
# <span id="forignRatioStr"></span>

fgn_own_ratio1 = soup.find_all('td', {'class':'cle r'})
fgn_own_ratio = fgn_own_ratio1[2].text
print(fgn_own_ratio)
# 46.71


# 6. 1Y 수익률
rel_return = float(soup.find_all("span", {"class":"tcr"})[2].text)
print(rel_return)
# 4.37


# 상단 테이블 웹 크롤링
up_list = soup.find("div", {"class":"corp_group2"})
# print(up_list)
ul = up_list.find_all("ul")
# print(ul)


# 7. PER(Price Earning Ratio: 주가수익비율)
per = float(up_list.find_all("li")[1].text)
print(per)
# 41.82


# 8. 12M PER (12개월 뒤의 예상 주가수익비율)
per_12m = float(up_list.find_all('li')[3].text)
print(per_12m)
# 4.57


# 9. 업종 PER
per_ind = float(up_list.find_all('li')[5].text)
print(per_ind)
# 31.68


# 10. PBR(Price to Book Ratio: 주가순자산비율)
# PBR = 주가/주당순자산
pbr = float(up_list.find_all('li')[7].text)
print(pbr)
# 4.29


# 11. 배당수익률(Dividend Yield)
div_yid1 = up_list.find_all('li')[9].text
div_yid2 = div_yid1.replace('%', '')
div_yid = float(div_yid2)
print(div_yid2)
# 0.61


# 시세현황 테이블 웹 크롤링
table1 = soup.find("div", {"id":"div1"})
table2 = table1.find_all("td")
print(table2)

# 12. 거래량
volume1 = table2[1].text
volume = int(volume1.replace(',', '').strip())
print(volume)
# 21669476

# 13. 거래대금
trans_price1 = table2[3].text
trans_price = int(trans_price1.replace(',', '').strip())
print(trans_price)
# 58745

# 14. 시가총액(우선주 포함)
mk_cpt_pfr1 = table2[6].text
mk_cpt_pfr = int(mk_cpt_pfr1.replace(',', '').strip())
print(mk_cpt_pfr)
# 17617473

# 15. 시가총액(보통주)
mk_cpt_cm1 = table2[8].text
mk_cpt_cm = int(mk_cpt_cm1.replace(',', '').strip())
print(mk_cpt_cm)
# 16048035

# 결과 모음
res = [date,
       corp_name,
       code,
       stock_price,
       fgn_own_ratio,
       rel_return,
       per, per_12m,
       per_ind, pbr,
       div_yid, volume,
       trans_price,
       mk_cpt_pfr,
       mk_cpt_cm]
print(res)