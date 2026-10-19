# game/__init__.py
# .graphic.render의 맨 앞 .은 현재 디렉터리를 의미한다.
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 여기에 패키지 초기화 코드를 작성한다.
print("Initializing game ...")