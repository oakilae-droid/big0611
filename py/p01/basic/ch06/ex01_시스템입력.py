# 시스템 입력
# inout()
print('메시지')
input('입력 메시지 기록')

# 사용자로부터 이름을 입력 
'''
이름을 입력하세요: 홍길동
'''

name = input('이름을 입력하세요:')
print(name + '님, 안녕하세요')

# 키에 따른 권장체중
# input 항상 문자열을 반환한다. -> int('184') -> 184
height = input('키를 입력하세요: ')
print('나의 키는 ' + height + 'cm 입니다.')
height = float(height)
weight = (height - 100) * 0.9
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print(당신의 권장 체중은 weight 입니다.)
print('당신의 권장체중은 ' + str(weight) + 'kg 입니다.')
# TypeError: can only concatenate str (not "float") to str
print('당신의 권장체중은 {}kg 입니다.'.format(weight))
# f-string
print(f'당신의 권장체중은 {weight}kg 입니다.')