# -*- coding: utf-8 -*-
from telnetlib import EC

import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import xlwt
import xdrlib, sys
import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait
from xlutils.copy import copy


# 新建一个xls用来存数据
excel = xlwt.Workbook(encoding='utf-8')  # 创建一个Excel
sheet = excel.add_sheet('Sheet1')  # 在其中创建一个名为hello的sheet
path = 'C:\\data5.xls'    # 每次运行都更改以避免覆盖上一轮数据
excel.save(path)


# 登录，需要破解算数验证码
# 可以暂时手动识别验证码
driver = webdriver.Firefox(executable_path='C:\\Users\Administrator\Desktop\geckodriver.exe')
driver.get("http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/tableSearch-showTableSearchIndex.shtml")
time.sleep(5)

driver.find_element_by_link_text(u"请登录").click()
driver.find_element_by_id("j_username").click()
driver.find_element_by_id("j_username").clear()
driver.find_element_by_id("j_username").send_keys("111111")
driver.find_element_by_id("j_password_show").click()
driver.find_element_by_id("j_password_show").clear()
driver.find_element_by_id("j_password_show").send_keys("1111111")
driver.find_element_by_id("j_validation_code").click()
validation = input("手动识别验证吧")
driver.find_element_by_id("j_validation_code").clear()
driver.find_element_by_id("j_validation_code").send_keys(validation)
driver.find_element_by_link_text(u"登录").click()
time.sleep(5)
driver.find_element_by_link_text(u"高级检索").click()
time.sleep(5)
driver.find_element_by_id("tableSearchItemIdIVDB020").click()
driver.find_element_by_id("tableSearchItemIdIVDB020").clear()
driver.find_element_by_id("tableSearchItemIdIVDB020").send_keys(u"电子科技大学")
driver.find_element_by_link_text(u"生成检索式").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='清空检索式'])[1]/following::a[1]").click()
time.sleep(20)
driver.find_element_by_id("txt").click()
driver.find_element_by_id("txt").clear()
# 在爬虫中断于870页后，我增加了page用于下次中断后的自动刷新定位页面重启爬虫
# 改变path，page之后可以重启爬虫
# 在哪一页中断就从哪一页开始
# page = 917
page = 1859
# page = 1832

js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

driver.find_element_by_id("txt").send_keys(page)
driver.find_element_by_link_text(u"确定").click()
time.sleep(15)
total = 0

while total < 70000:
    driver.maximize_window()
    total = total + 1
    # 本条数据需要写入xls
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(12):
        # 爬取一个页面的内容
        html = driver.page_source
        soup = BeautifulSoup(html)
        # 专利名
        items_b = soup.find_all('b', attrs={'style': "color: #4B4B4B"})
        item_b = items_b[i]
        # print(item_b.text)
        # 公开号
        items_number = soup.find_all('a', attrs={'class': "btn btn-operation", 'role': "lawState"})
        # print(items_number[i].get('pn'))
        # 摘要描述
        items_abview = soup.select('.abview-content')
        # print(items_abview[i].text)
        # proposer
        proposer = soup.find_all('a', attrs={'href': "javascript:;",
                                             'onclick': "drillSearch('IVDB020','申请（专利权）人','','false',this);return false;"})
        # print(proposer[i].text)
        # IPC
        y = i + 1
        time.sleep(1)
        try:
            e = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='公开（公告）日 :'])[%s]/following::p[1]" % y).text
        except:
            time.sleep(5)
            continue
        # print(e)

        new_worksheet.write(i + rows_old, 0, item_b.text)  # 追加写入数据，注意是从i+rows_old行开始写入,第0列写专利名
        new_worksheet.write(i + rows_old, 1, items_number[i].get('pn'))  # 公开号
        try:
            new_worksheet.write(i + rows_old, 2, items_abview[i].text)  # 摘要
        except:
            continue
        new_worksheet.write(i + rows_old, 3, proposer[i].text)  # 申请人
        try:
            new_worksheet.write(i + rows_old, 4, e)  # IPC
        except:
            continue
    new_workbook.save(path)  # 保存工作簿

    # 点击下一页
    time.sleep(1)
    try:
        # time.sleep(3)


        # # try:
        # wait.until(EC.invisibility_of_element_located([By.XPATH,
        #                                                "//div[@class='blockUI blockOverlay']"]))
        #
        # driver.find_element_by_link_text(u"下一页").click()
        # # except:
        element: WebElement = driver.find_element_by_link_text(u"下一页")
        driver.execute_script('arguments[0].click();', element)
        page = page+1
    except:
        driver.maximize_window()
        print(str(page)+'page')
        driver.refresh()  # 刷新
        time.sleep(15)
        driver.find_element_by_link_text(u"高级检索").click()
        time.sleep(5)
        driver.find_element_by_id("tableSearchItemIdIVDB020").click()
        driver.find_element_by_id("tableSearchItemIdIVDB020").clear()
        driver.find_element_by_id("tableSearchItemIdIVDB020").send_keys(u"电子科技大学")
        driver.find_element_by_link_text(u"生成检索式").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='清空检索式'])[1]/following::a[1]").click()
        driver.maximize_window()
        time.sleep(20)
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_id("txt").click()
        driver.find_element_by_id("txt").clear()
        page_string = str(page+1)
        # 1787页中断，并且发现1786页缺少最后一条，于是决定从1786页从新开始，可能会重复一页，但不遗漏
        # 重复检查时发现1786页已经爬取完毕，是重复爬取的第二遍缺少一条数据，因此应删除这组数据，从page+1开始
        driver.find_element_by_id("txt").send_keys(page_string)
        driver.find_element_by_link_text(u"确定").click()
        time.sleep(10)
        continue
    time.sleep(7)

