from selenium import webdriver

url = "http://www.naver.com/"

browser = webdriver.Chrome()

browser.implicitly_wait(3)

browser.get(url)

browser.save_screenshot("Website.png")

browser.quit()
