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

# import 모듈 as qufcld
import diet as dt
dt.get_recommend_weight(160)
dt.print_valid_menu()
print(dt.menu)

# from 모듈 import 함수, 변수, 모듈
from diet import get_recommend_weight, print_valid_menu
get_recommend_weight(160, False)
