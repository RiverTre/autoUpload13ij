from selenium import webdriver # pycharm的话点击这一行就会出现小灯泡，在这里安装selenium也可以
import time

# 用于将已经审核过的组合上架

# 火狐浏览器webdriver解压后的地址
driver = webdriver.Firefox(executable_path='I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')

driver.get('http://patentshop.13ij.net/')
driver.find_element_by_id("mobile1").click()
driver.find_element_by_id("mobile1").clear()
driver.find_element_by_id("mobile1").send_keys("17362997735")
driver.find_element_by_id("button").click()
mobileCode = input('在这里输入验证码')
driver.find_element_by_id("mobileCode").click()
driver.find_element_by_id("mobileCode").clear()
driver.find_element_by_id("mobileCode").send_keys(mobileCode)
driver.find_element_by_id("login2").click()
time.sleep(1.5)
while bool(1):
    try:

        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='待上架'])[2]/following::button[1]").click()
    except:
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='上一页'])[1]/following::button[1]").click()
        continue