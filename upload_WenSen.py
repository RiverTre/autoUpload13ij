# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import xlrd

#打开EXCEL
data = xlrd.open_workbook('Z:\\test-兰州大学v-文森.xlsx')
table = data.sheets()[0]
nrows = table.nrows #行数
ncols = table.ncols #列数

#不同大学程序差异在于 分类三次点击 图标选择的id 用户名密码 .XLSX文件存放位置
#不同电脑之间，四张图片存放的位置不同，需要重新编译exe
driver = webdriver.Firefox(executable_path = 'I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get("http://patentbusiness.13ij.net/account/login.htm;jsessionid=040D4C5FE9C730550E49AC2699FACB5B")
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("111111111")
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1111111111")
driver.find_element_by_id("login").click()
time.sleep(5)
driver.find_element_by_link_text(u"+添加商品").click()
for i in range(nrows):#nrows为边界，不包括nrows
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='确定添加'])[1]/following::div[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='一级分类'])[1]/following::select[1]").click()
    Select(driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='一级分类'])[1]/following::select[1]")).select_by_visible_text(
        u"制造业")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='一级分类'])[1]/following::option[4]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='二级分类'])[1]/following::select[1]").click()
    Select(driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='二级分类'])[1]/following::select[1]")).select_by_visible_text(
        u"其他制造业")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='二级分类'])[1]/following::option[18]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类'])[1]/following::select[1]").click()
    Select(driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类'])[1]/following::select[1]")).select_by_visible_text(
        u"其他制造业")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类'])[1]/following::option[2]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='选择机构'])[1]/following::img[153]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='选择机构'])[1]/following::div[2]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品名称'])[1]/following::input[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品名称'])[1]/following::input[1]").clear()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品名称'])[1]/following::input[1]").send_keys(table.col(0)[i].value)
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品型号'])[2]/following::input[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品型号'])[2]/following::input[1]").clear()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品型号'])[2]/following::input[1]").send_keys(table.col(1)[i].value)
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::textarea[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::textarea[1]").clear()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::textarea[1]").send_keys(table.col(2)[i].value)
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::div[2]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='*图片尺寸：宽600px-800px,高度和宽度一致,大小不超过5M！'])[1]/following::div[3]").click()
    time.sleep(1)
    os.system(r'E:\autoitTest_1.exe')
    time.sleep(3)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::div[1]").click()
    time.sleep(1)
    os.system(r'E:\autoitTest_2.exe')
    time.sleep(3)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='-'])[2]/following::div[1]").click()
    time.sleep(1)
    os.system(r'E:\autoitTest_3.exe')
    time.sleep(3)
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='*图片尺寸：宽度800px-1200px，高度不限，大小不超过5M！'])[1]/following::div[3]").click()
    time.sleep(1)
    os.system(r'E:\autoitTest_4.exe')
    time.sleep(3)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='+'])[2]/following::div[1]").click()
    time.sleep(10)

    driver.maximize_window()

    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='保存'])[1]/following::div[2]").click()
#下面再次点击没有想要的商品手动添加
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='确定添加'])[1]/following::div[1]").click()