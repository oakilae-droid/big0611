import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 2000ms(1초)마다 페이지 자동 새로고침
# st_autorefresh(interval=2000, key='datarefresh')
st_autorefresh()

st.title('안녕 Streamlit!!')
st.write('첫 번째 Streamlit 애플리케이션입니다.')

# 1. 제목과 헤더 만들기
st.title('이것이 가장 큰 제목입니다.')  # 2.75rem = 44px
st.header('이것은 큰 헤더입니다.')  # 2.25rem = 36px
st.subheader('이것은 작은 헤더입니다.')  # 1.5rem = 24px

# 2. 일반 텍스트 표시하기
st.text('이것은 일반적인 텍스트입니다.')   # 1rem = 16px
st.text('여러 줄로 텍스트를 작성할 수도 있습니다.')

# 3. 마크다운으로 꾸미기
st.markdown('**이것은 굵은 글씨입니다.**')
st.markdown('*이것은 기울어진 글씨입니다.*')
st.markdown('이것은 `인라인 코드` 입니다.')

# 4. 만능 출력 함수
st.write('안녕하세요!')
st.write(123)
st.write([1, 2, 3, 4, 5])

# 입력 컴포넌트
# 1. 선택 상자 만들기
# 좋아하는 과일 선택
fruit = st.selectbox(
    '좋아하는 과일을 선택하세요:',
    ['사과', '바나나', '오렌지', '포도']
)
st.write(f'당신이 선택한 과일은 {fruit} 입니다.')

# 2. 텍스트 입력받기
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이를 입력하세요', min_value=0, max_value=120)

if name and age:
    st.write(f'{name}님은 {age}살입니다.')

# 3. 슬라이드로 값 조정하기 <input type="range">
temperature = st.slider('온도를 선택하세요', 0, 40, 25)
st.write(f'선택한 온도는 {temperature}도 입니다.')

# 4. 라디오 버튼과 체크박스 <input type="radio|checkbox">
color = st.radio(
    '좋아하는 색갈을 선택하세요',
    ['빨강', '파랑', '초록']
)

agree = st.checkbox('이용약관에 동의합니다.')
if agree:
    st.write('동의해주셔서 감사합니다.')

# 5. 여러 개 선택하기
hobbies = st.multiselect(
    '취미를 선택하세요. (여러 개 선택 가능)',
    ['독서', '영화감상', '운동', '여행', '음악감상']
)

if hobbies:
    st.write('선택한 취미:', hobbies)

# 6. 날짜와 시간 입력
today = st.date_input('날짜를 선택하세요.')
current_time = st.time_input('시간을 선택하세요')

st.write(f'선택한 날짜: {today}')
st.write(f'선택한 시간: {current_time}')

# 미디어 컴포넌트
# 1. 이미지 표시하기 
# <img src="경로/파일명" width=300 alt="대체텍스트">
# 비트맵(jpg, gif, png), 벡터(svg)
# 인터넷 이미지 표시
# https://picsum.photos -> 더미이미지(랜덤 사진)
# https://unsplash.com/ko -> 사진
# https://www.dummyimage.com/
# https://www.pngwing.com/ko -> 심볼, 아이콘
st.image('https://picsum.photos/200/300', caption='인터넷 이미지')
# st.image('https://en, caption='부동산', width=300)

# 로컬 이미지 파일 표시(파일이 있는 경우)
st.image('my_image.jpg', caption='내 이미지', width=300)
st.image('unsplash.jpg', caption='아파트', width=300)
st.image('pngwing.png', caption='아이콘')

# 비디오 파일 재생 
# <video src="경로/파일명"></video>
# mp4, webm, ogv(ogg)
st.video('my_video.mp4', width=300)

# 유튜브 비디오 표시 <iframe src="경로/파일명"></iframe>
st.video('https://youtu.be/BU-DXvjGEqg?si=pEbyz3fKnu8LG4NG', width=300)

# 오디오 파일 재생
# 무료 소리 창고: https://pgtd.tistory.com/270
# mp3(노래), ogg(ogv), wav(미디음)

st.audio('ding.mp3')
st.audio('my_audio.mp3')