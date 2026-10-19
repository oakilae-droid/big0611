# render.py
# from game.sound.echo import echo_test
# 상대경로 패키지
from ..sound.echo import echo_test
# ..은 render.py 파일의 부모 디렉터리를 의미한다.

def render_test():
    print("render")
    echo_test()