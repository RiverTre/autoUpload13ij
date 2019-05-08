from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement

# 提交组合后，用于审核组合

driver = webdriver.Firefox(executable_path = 'I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get("http://patentadmin.13ij.net/")
driver.find_element_by_id("mobile").click()
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("15012123612")
driver.find_element_by_id("verifyCode").click()
driver.find_element_by_id("verifyCode").clear()
driver.find_element_by_id("verifyCode").send_keys("123456")
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("a123456")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='管理员密码'])[1]/following::button[1]").click()
time.sleep(2)
driver.find_element_by_link_text(u"商品管理").click()
time.sleep(1)
driver.find_element_by_link_text(u"店铺商品").click()
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'/goods/sgoods/list.iframe')]"))
driver.find_element_by_id("bshop").click()
driver.find_element_by_id("bshop").clear()
# 大学名改成自己的
driver.find_element_by_id("bshop").send_keys(u"电子科技大学")
driver.find_element_by_id("button1").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='审核状态：'])[1]/following::i[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='不限'])[2]/following::dd[1]").click()

while bool(1):
    time.sleep(1)
    element: WebElement = driver.find_element_by_link_text(u"审核组合")
    driver.execute_script('arguments[0].click();', element)
    time.sleep(0.7)
    driver.find_element_by_link_text(u"确定").click()