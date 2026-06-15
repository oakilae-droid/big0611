# 자료형
# 1. 숫자형
# 정수
x, y = 10, -25
# 실수
z = 3.14
# print(): 터미널에 출력 내장 함수
# type(): 자료형 확인 내장 함수
print(type(x), type(y), type(z))

# 지수 표현식(e: exponential)
# e3 -> 10의 3승 -> 10*10*10
# 대소문자 구별 없음
# 17 곱하기 10의 3승
a = 17e3
b = 17E3
c = -35.2e2
d = 275e-2
print(a, b, c, d)

# 2. 불리언: (예약어) True, False -> 논리값
# 대입 연산자: =
# 비교 연산자: > < ==
a = 100> 50
b = 100< 50
c = 100 == 50
print(a, b, c)
type(a)

# 3. 문자형(str): "", ''
a = "Hello" 
b = '1234'
c = 'How are you?'
# 다중 커서: ctrl+alt+위아래방향키 또는 alt+클릭 
print(type(a))
print(type(b))
print(type(c))

# 다중 행 문자열(''', """)
x = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""
print(x)

y = "Twinkle, twinkle, little star,\
How I wonder what you are!\
Up above the world so high,\
Like a diamond in the sky."
print(y)

'''
데이터 타입
1) 기본 데이터
    - 숫자(int, float)
    - 문자(str)
    - 불(bool)
2) 복합 데이터
'''

# 타입 변환
# int(), float(), str(), bool()
temperature = '20'
humidity = '50'
print(temperature + humidity)
print(int(temperature) + int(humidity))

a = 0           # False
b = 500         # True -> 0 이외의 숫자는 모드 True
c = ''          # 빈값 -> False
d = '하하호호'  # True
e = None        # False
print(bool(a), bool(b), bool(c), bool(d), bool(e))

