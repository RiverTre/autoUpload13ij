from selenium import webdriver # pycharm的话点击这一行就会出现小灯泡，在这里安装selenium也可以
import time
import os

# 店长中心，自动添加组合，以便后台审核专利组合

# 火狐浏览器webdriver解压后的地址
driver = webdriver.Firefox(executable_path='I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')

driver.get('http://patentshop.13ij.net/')
driver.find_element_by_id("mobile1").click()
driver.find_element_by_id("mobile1").clear()
driver.find_element_by_id("mobile1").send_keys("17362997735")
driver.find_element_by_id("button").click()
mobileCode = input('输入验证码')
driver.find_element_by_id("mobileCode").click()
driver.find_element_by_id("mobileCode").clear()
driver.find_element_by_id("mobileCode").send_keys(mobileCode)
driver.find_element_by_id("login2").click()
time.sleep(1.5)
driver.find_element_by_link_text(u"上架新商品").click()
page = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上一页'])[1]/following::span[1]").text
page = page[2:]
page = int(page)
for i in range(page+1):

    time.sleep(2)
    driver.find_element_by_class_name('saleGoods').click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::img[1]").click()

    # os 上传
    # 关于autoit上传图片，若读完下列说明仍旧疑惑可以参看README的教程。
    # 安装好autoIT，用装好后的SciTE Script Editor打开一个.au3文件，把图片地址更改为自己存放    专利分析报告.jpg    的地址
    # 保存，打开Compile Script to exe， 把.au3选进去，convert
    # 下面这行代码是exe的地址
    # 后边还有两行os.system(),同理，分别是行业技术报告.jpg以及专利主图.jpg
    os.system(r'E:\autoit_a.exe')
    time.sleep(2)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").send_keys(u"专利+专利分析报告")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").send_keys("20000")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").send_keys("1")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::button[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::img[1]").click()

    os.system(r'E:\autoit_b.exe')
    time.sleep(2)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").send_keys(u"专利+行业技术报告")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").send_keys("20000")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").send_keys("1")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::button[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::img[1]").click()
    os.system(r'E:\autoitTest_1.exe')
    time.sleep(2)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[2]").send_keys(u"专利")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[3]").send_keys("10000")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::input[4]").send_keys("1")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::button[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[3]/following::button[1]").click()