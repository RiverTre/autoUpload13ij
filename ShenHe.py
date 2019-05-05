# -*- coding: utf-8 -*-
# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import unittest, time, re

driver = webdriver.Firefox(executable_path = 'I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
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
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='管理员密码'])[1]/following::button[1]").click()
time.sleep(2)
driver.find_element_by_link_text(u"商品管理").click()
time.sleep(1)
driver.find_element_by_link_text(u"公共商品").click()
time.sleep(1)
# ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
i = 0
driver.maximize_window()
# driver.execute_script("document.body.style.zoom='80%';")
# num = 0.8
# js = "document.body.style.zoom='%s';" % num
# driver.execute_script(js)

count=0
while i < 1000:
    # # driver.switch_to.frame(1)
    # driver.find_element_by_link_text(u"确认审核").click()
    # time.sleep(0.5)
    # driver.find_element_by_link_text(u"确定").click()
    # time.sleep(0.5)

    # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
    try:

        driver.refresh()
        driver.find_element_by_link_text(u"商品管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"公共商品").click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'/goods/goods/list.iframe')]"))

        time.sleep(1)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='创建时间'])[1]/following::i[3]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='搜索'])[1]/following::button[1]").click()
        driver.find_element_by_link_text(u"确定").click()
    except:
        time.sleep(0.5)
        print(str(i))
        count = count+1
        if count > 10:
            break
        continue
