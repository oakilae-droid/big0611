# 1. 데이터를 표로 보여주기
import streamlit as st
import pandas as pd

# 학생 성적 데이터 만들기
data = {
    '이름': ['홍길동', '김길동', '박기흥', '이미금'],
    '수학': [85, 92, 78, 86],
    '영어': [88, 85, 90, 93],
    '과학': [90, 88, 85, 89]
}

# 데이터 분석
df = pd.DataFrame(data)

# 웹 브라우저 표시할 콘텐츠
st.title('학생 성적 데이터 표시하기')
st.dataframe(df)

# 온라인 쇼핑몰 판매 데이터
sales_data = {
    '상품명': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    '가격': [1200000, 25000, 80000, 350000, 150000],
    '판매량': [15, 120, 85, 30, 45],
    '평점': [4.5, 4.2, 4.7, 4.1, 4.6]
}

df = pd.DataFrame(sales_data)

# 평점에 따라 색깔 적용
def color_rating(val):
    if val >= 4.5:
        color = 'greeen'
    elif val >= 4.0:
        color = 'orange'
    else:
        color = 'red'
    return f'color: {color}'


# 스타일 적용해서 표시
# pandas 2.1.0 버전부터 applymap() -> map()
# pandas 3.0.3
styled_df = df.style.format({
    '가격': '{:,}원',
    '판매량': '{:,}개',
    '평점': '{:.1f}점'
}).map(color_rating, subset=['평점'])

st.dataframe(styled_df)