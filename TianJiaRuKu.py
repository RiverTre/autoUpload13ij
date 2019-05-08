from selenium import webdriver
import time

# 将已经上传的商品添加到自己的商品库

# 火狐webdriver的zip下载后的解压路径
driver = webdriver.Firefox(executable_path='I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')

driver.get("http://patentbusiness.13ij.net/account/login.htm;jsessionid=040D4C5FE9C730550E49AC2699FACB5B")
driver.find_element_by_id("mobile").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("改成自己的密码")
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("你的手机号")
driver.find_element_by_id("login").click()
time.sleep(2)




gogogo = bool(1)
while gogogo:

    # 选择机构
    time.sleep(1)
    driver.find_element_by_link_text(u"+添加商品").click()

    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品机构：'])[1]/following::i[1]").click()
    
    # 点击“商品机构”后在网页下拉列表里数好自己的logo是第多少个，电子科技大学是217，把下面这个217替换成自己的数字
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
    try:
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
    except:
        print('Ouch!')
        continue



