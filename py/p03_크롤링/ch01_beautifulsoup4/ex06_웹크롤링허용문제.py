# 웹 크롤링 허용문제
# robots.txt는 크롤링하는 데 필요한 규칙을 정리해 놓은 페이지다.
# https://www.google.com/robots.txt

rp = RobotFilePaser()
# 확인하려는 사이트의 robots.txt 주소 입력
rt.set_url("https://www.google.com/robots.txt")

# 내 크롤로봇(*)이 특정 URL을 긁어도 되는지 확인 (True/False)