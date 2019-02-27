# 60페이지
# 로그인을 위한 모듈 추출하기
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정하기
USER = "juciii96"
PASS = "tjdwn0907^"

# 세션 시작하기
session = requests.session()
# 로그인하기
login_info = {
    "m_id": USER,
    "m_passwd": PASS
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)# 로그인 시켜주는 함수
res.raise_for_status() # 오류가 발생하면 예외가 발생합니다.

# 마이페이지에 접근하기
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 > dd > span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지: " + mileage)
print("이코인: " + ecoin)