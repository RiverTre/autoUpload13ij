from selenium import webdriver
import time

# 将已经上传的商品添加到自己的商品库
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path='I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get("http://patentbusiness.13ij.net/account/login.htm;jsessionid=040D4C5FE9C730550E49AC2699FACB5B")
driver.find_element_by_id("mobile").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("密码")
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("手机号")
driver.find_element_by_id("login").click()
time.sleep(2)




gogogo = bool(1)
while gogogo:



    # # 隐式等待
    # driver.implicitly_wait(5)
    # try:
    #     print(time.ctime())
    #     driver.find_element_by_link_text(u"+添加商品").click()
    # except NoSuchElementException as e:
    #     print(e)
    #     continue
    # finally:
    #     print(time.ctime())



    # 显式等待

    #     wait = ui.WebDriverWait(driver, 10)
    #     wait.until(lambda driver: driver.find_element_by_link_text(u"+添加商品"))
    # except:
    #     print('timeout~')
    #     driver.refresh()
    #     continue
    # driver.find_element_by_link_text(u"+添加商品").click()
    element = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, "+添加商品"))
    )
    element.click()

    # 选择机构

    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品机构：'])[1]/following::i[1]").click()
    # 数好自己的logo是第多少个，电子科技大学是217，把下面这个217替换成自己的数字
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类：'])[1]/following::span[217]").click()
    time.sleep(2)


    # 获取总页数
    total_page_string = driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::b[1]").text
    total_page = int(total_page_string)
    total_page = total_page - 1
    if total_page <= 1:
        break
    total_page_string = str(total_page)

    # 跳转到最后一页
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::input[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::input[1]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::input[1]")\
        .send_keys(total_page_string)
    time.sleep(1)
    driver.find_element_by_link_text(u"确定").click()


    # 选择item并点击确定添加

    # 等待元素出现
    max_attemps = 10
    while True:
        itemAppear = driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='全选'])[1]/following::i[1]")
        if itemAppear is not None:
            break
        else:
            time.sleep(0.5)
            max_attemps -= 1
        if max_attemps == 0:
            driver.fail("Cannot find element.")
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='全选'])[1]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[1]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[2]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[3]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[4]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[5]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[6]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[7]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[8]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='审核通过'])[9]/following::i[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[1]/following::div[3]").click()

    # total_page = total_page - 1
    # total_page_string = str(total_page)


