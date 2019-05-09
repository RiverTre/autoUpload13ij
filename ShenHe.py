# -*- coding: utf-8 -*-
from selenium import webdriver
import time

# 审核商品
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# option_path="user-data-dir=D:\\Users\\yuehan\\AppData\\Local\\Google\\Chrome\\User Data"
# option = Options()
# option.add_argument(option_path)
# driver = webdriver.Chrome(executable_path="I:\Downloads\chromedriver_win32\\chromedriver.exe", chrome_options=option)

driver = webdriver.Firefox(executable_path='I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get("http://patentadmin.13ij.net/")
# html = driver.page_source
# # html.send_keys(Keys.chord(Keys.CONTROL, Keys.SUBTRACT))
#


driver.find_element_by_id("mobile").click()
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("15012123612")
driver.find_element_by_id("verifyCode").click()
driver.find_element_by_id("verifyCode").clear()
driver.find_element_by_id("verifyCode").send_keys("123456")
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("a123456")
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='管理员密码'])[1]/following::button[1]").click()
time.sleep(2)
driver.find_element_by_link_text(u"商品管理").click()
time.sleep(1)
element6 = WebDriverWait(driver, 100, 0.5).until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "公共商品")))
driver.execute_script('arguments[0].click();', element6)
time.sleep(1)
# ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
i = 0
driver.maximize_window()


# driver.execute_script("document.body.style.zoom='80%';")
# num = 0.8
# js = "document.body.style.zoom='%s';" % num
# driver.execute_script(js)
def start():
    driver.refresh()
    driver.find_element_by_link_text(u"商品管理").click()

    element1 = WebDriverWait(driver, 100, 0.5).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,
                                                                                                      "公共商品"))
                                                     )
    element1.click()
    element2 = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH,
                                                         "//iframe[contains(@src,'/goods/goods/list.iframe')]"))
    )
    driver.switch_to.frame(element2)


start()
count = 0
while i < 1000:

    time.sleep(1)
    element3 = WebDriverWait(driver, 5, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH,
                                                         u"(.//*[normalize-space(text()) and normalize-space("
                                                         u".)='创建时间'])[1]/following::i[3]"))
    )
    # 从element.click()换成了js
    driver.execute_script('arguments[0].click();', element3)
    time.sleep(0.5)
    element4 = WebDriverWait(driver, 5, 0.5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, u"(.//*[normalize-space(text()) and normalize-space(.)='搜索'])[1]/following::button[1]")))

    element4.click()
    try:

        element5 = WebDriverWait(driver, 5, 0.5).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, u"确定")))
        # ec方法是两参数的，所以最后的By....要打括号作为一个参数输入
        element5.click()
        time.sleep(0.5)
    except:
        start()
        continue
