# 모듈
# diet.py
'''
변수: menu
함수: 
    get_recommend_weight(height, ma=True)
    print_valid_menu()
'''
# import 모듈
import diet
# 모듈.함수
diet.get_recommend_weight(160, False)

# import 모듈 as 별칭(내가 별칭을 붙여줘서 긴 모듈 이름을 편하게 계속 쓰기 위해)
import diet as dt
dt.get_recommend_weight(160)
dt.print_valid_menu()
print(dt.menu)

# from 패키지 import 모듈A, 모듈B
# from 모듈 import 함수, 변수
# (모듈이나 패키지에 특정 함수만 사용하고자 할때)
from diet import get_recommend_weight, print_valid_menu
get_recommend_weight(160, False)
