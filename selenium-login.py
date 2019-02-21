from selenium import webdriver
from selenium.webdriver.common.keys import Keys
USER = 'rlawlsdud0419'
PASS = 'kjy89970!@'
INFORM = '성주오빠 바보'
browser = webdriver.Chrome()
browser.implicitly_wait(3)

url_login = "https://accounts.google.com/AddSession/identifier?hl=ko&continue=https%3A%2F%2Fwww.google.com%2Fwebhp%3Fhl%3Dko%26ictx%3D2%26sa%3DX%26ved%3D0ahUKEwjskOisrc3gAhXXx4sBHX3EBTsQPQgH&flowName=GlifWebSignIn&flowEntry=AddSession"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e = browser.find_element_by_id("identifierId")
e.clear()
e.send_keys(USER)
e.send_keys(Keys.ENTER)
e = browser.find_element_by_name("password")
e.clear()
e.send_keys(PASS)
e.send_keys(Keys.RETURN)
e=browser.find_element_by_name("q")
e.clear()
e.send_keys(INFORM)
e.send_keys(Keys.RETURN)
# form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
# form.submit()
print("로그인 버튼을 클릭합니다.")

# browser.quit()

#
# browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
#
# products = browser.find_elements_by_css_selector(".p_info span")
# print(products)
# for product in products:
#     print("-", product.text)