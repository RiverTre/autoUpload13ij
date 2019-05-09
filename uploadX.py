# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
import os
import xlrd
from selenium.webdriver.common.action_chains import ActionChains

# 打开EXCEL
from selenium.webdriver.support.wait import WebDriverWait

data = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\file3b.xls')
table = data.sheets()[0]
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数

# 不同大学程序差异在于 分类三次点击 图标选择的id 用户名密码 .XLSX文件存放位置
# 不同电脑之间，四张图片存放的位置不同，需要重新编译exe
driver = webdriver.Firefox(executable_path = 'C:\\Users\Administrator\Desktop\geckodriver.exe')
driver.get("http://patentbusiness.13ij.net/account/login.htm;jsessionid=040D4C5FE9C730550E49AC2699FACB5B")
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("17362997735")
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("aaaaaaaa")
driver.find_element_by_id("login").click()
time.sleep(5)
driver.find_element_by_link_text(u"+添加商品").click()
i = 29
for i in range(nrows):  # nrows为边界，不包括nrows

    # try:
    element = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH,
                                                        u"(.//*[normalize-space(text()) and normalize-space(.)='确定添加'])[1]/following::div[1]")))
    driver.execute_script('arguments[0].click();', element)
    element1 = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH,
        u"(.//*[normalize-space(text()) and normalize-space(.)='一级分类'])[1]/following::select[1]")))
    driver.execute_script('arguments[0].click();', element1)
    # except:
    #     driver.refresh()
    #     time.sleep(1)
    #     driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
    #     print('alpha' + str(i))
    #     i = i - 1
    #     continue
    # 分类
    ipc = str(table.col(3)[i])
    ipc = ipc[-3:-1]
    # print(ipc)
    classes = ''
    if ipc == 'A0':
        classes = ["农林渔业", "农业", "其他农业"]
    elif ipc == 'A2':
        classes = ["农林渔业", "畜牧业", "其他畜牧业"]
    elif ipc == 'A4':
        classes = ["制造业", "服饰业", "服饰制造"]
    elif ipc == 'A6' or ipc == 'B6' or ipc == 'B8':
        classes = ["制造业", "其他制造业", "其他制造业"]
    elif ipc == 'B0' or ipc == ('B2'):
        classes = ["制造业", "通用设备制造业", "其他设备制造"]
    elif ipc == 'B3' or ipc == ('B4'):
        classes = ["制造业", "文教用品", "办公用品制造"]
    elif ipc == 'C0' or ipc == ('C1') or ipc == ('C2') or ipc == ('C3'):
        classes = ["制造业", "化学制品", "专用化学产品"]
    elif ipc == 'D0' or ipc == ('D2'):
        classes = ["制造业", "纺织业", "家用纺织制造"]
    elif ipc == 'E0' or ipc == ('E2'):
        classes = ["建筑业", "其他建筑业", "其他建筑行业"]
    elif ipc == 'F0' or ipc == ('F1') or ipc == ('F2') or ipc == ('F4'):
        classes = ["制造业", "通用设备制造业", "机械加工制造"]
    elif ipc == 'G0' or ipc == ('G1'):
        classes = ["制造业", "仪器仪表制造", "通用仪器仪表"]
    elif ipc == 'H0':
        classes = ["制造业", "电器机械", "其他电器机械"]
        # print(classes)
    else:
        classes = ["信息服务", "互联网服务", "互联网信息服务"]
    option = 0

    try:
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='一级分类'])[1]/following::select[1]")
               ).select_by_visible_text(u"%s" % (classes[0]))
    except:
        driver.refresh()
        time.sleep(1)
        driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
        print('beta' + str(i))
        i = i - 1
        continue
    if classes[0] == "制造业":
        option = 3
    elif classes[0] == "信息服务":
        option = 7
    elif classes[0] == "建筑业":
        option = 5
    elif classes[0] == "农林渔业":
        option = 1
    try:
        element2 = driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='一级分类'])[1]/following::option[%s]" % (option + 1))
        driver.execute_script('arguments[0].click();', element2)
        element3 = driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='二级分类'])[1]/following::select[1]")
        driver.execute_script('arguments[0].click();', element3)
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='二级分类'])[1]/following::select[1]")
        ).select_by_visible_text(u"%s" % (classes[1]))
    except:
        driver.refresh()
        time.sleep(1)
        driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
        print('beta' + str(i))
        i = i - 1
        continue
    if classes[1] == "农业":
        option = 1
    elif classes[1] == "畜牧业":
        option = 3
    elif classes[1] == "服饰业":
        option = 5
    elif classes[1] == "其他制造业":
        option = 17
    elif classes[1] == "通用设备制造业":
        option = 11
    elif classes[1] == "文教用品":
        option = 6
    elif classes[1] == "化学制品":
        option = 7
    elif classes[1] == "纺织业":
        option = 4
    elif classes[1] == "其他建筑业":
        option = 4
    elif classes[1] == "仪器仪表制造":
        option = 16
    elif classes[1] == "电器机械":
        option = 14
    elif classes[1] == "互联网服务":
        option = 1
    try:
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='二级分类'])[1]/following::option[%s]" % (
                        option + 1)).click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类'])[1]/following::select[1]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类'])[1]/following::select[1]")
        ).select_by_visible_text(u"%s" % (classes[2]))
    except:
        driver.refresh()
        time.sleep(1)
        driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
        # driver.find_element_by_link_text(u"+添加商品").click()
        print(str(i))
        i = i - 1
        continue

    if classes[2] == "其他农业":
        option = 6
    elif classes[2] == "其他畜牧业":
        option = 4
    elif classes[2] == "服饰制造":
        option = 2
    elif classes[2] == "其他制造业":
        option = 1
    elif classes[2] == "其他设备制造":
        option = 7
    elif classes[2] == "办公用品制造":
        option = 1
    elif classes[2] == "专用化学产品":
        option = 3
    elif classes[2] == "家用纺织制造":
        option = 3
    elif classes[2] == "其他建筑行业":
        option = 2
    elif classes[2] == "机械加工制造":
        option = 2
    elif classes[2] == "通用仪器仪表":
        option = 4
    elif classes[2] == "其他电器机械":
        option = 4
    elif classes[2] == "互联网信息服务":
        option = 1

    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='三级分类'])[1]/following::option[%s]" % (
                    option + 1)).click()

    # 下一行的img[217]指的是电子科技大学的logo，为第217个，若logo位于第一行第一列，则为img[1]
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='选择机构'])[1]/following::img[217]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='选择机构'])[1]/following::div[2]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品名称'])[1]/following::input[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品名称'])[1]/following::input[1]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品名称'])[1]/following::input[1]").send_keys(
        table.col(0)[i].value)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品型号'])[2]/following::input[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品型号'])[2]/following::input[1]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品型号'])[2]/following::input[1]").send_keys(
        table.col(1)[i].value)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::textarea[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::textarea[1]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::textarea[1]").send_keys(
        table.col(2)[i].value)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='商品描述'])[1]/following::div[2]").click()
    try:
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='*图片尺寸：宽600px-800px,"
                                 u"高度和宽度一致,大小不超过5M！'])[1]/following::div[3]").click()
    except:
        print('似乎已有')
        continue
    time.sleep(0.5)
    os.system(r'C:\\Users\Administrator\Desktop\autoitTest_1.exe')

    # 等图片传完点一下，皮一下非常开心
    elemente = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH, (u"(.//*[normalize-space(text()) and normalize-space(.)='*图片尺寸：宽600px-800px,高度和宽度一致,大小不超过5M！'])[1]/following::img[1]"))))
    elemente.click()

    element4 = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH, (
            "(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::div[1]"))))
    element4.click()
    time.sleep(0.7)
    os.system(r'C:\\Users\Administrator\Desktop\autoitTest_2.exe')
    elementee = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH, (
            ("(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::img[1]")))))
    elementee.click()
    element5 = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='-'])[2]/following::div[1]")))
    element5.click()
    time.sleep(0.7)
    os.system(r'C:\\Users\Administrator\Desktop\autoitTest_3.exe')
    elementeee = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH, (
            ("(.//*[normalize-space(text()) and normalize-space(.)='-'])[2]/following::img[1]")))))
    elementeee.click()
    element6 = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH,
                                                         u"(.//*[normalize-space(text()) and normalize-space("
                                                         u".)='*图片尺寸：宽度800px-1200px，高度不限，大小不超过5M！'])["
                                                         u"1]/following::div[3]")))
    element6.click()
    time.sleep(0.7)
    os.system(r'C:\\Users\Administrator\Desktop\autoitTest_4.exe')
    try:

        elementeeee = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH, (
            (u"(.//*[normalize-space(text()) and normalize-space(.)='*图片尺寸：宽度800px-1200px，高度不限，大小不超过5M！'])[1]/following::img[1]")))))
    except:
        driver.refresh()
        time.sleep(1)
        print("timeout")
        i = i - 1
        driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
        continue
    elementeeee.click()
    element7 = WebDriverWait(driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='+'])[2]/following::div[1]")))
    element7.click()
    driver.maximize_window()

    try:
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='保存'])[1]/following::div[2]").click()
    except:
        driver.refresh()
        time.sleep(1)
        driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
        continue

    # 点击确定，还是没法点击，暂时不管了，可以用异常处理刷新一下，异常处理在上边
    # element8 = WebDriverWait(driver, 100, 0.5).until(
    #     expected_conditions.presence_of_element_located(
    #         (By.XPATH, u"(.//*[normalize-space(text()) and normalize-space(.)='保存'])[1]/following::div[2]")))
    # ActionChains(driver).move_to_element(element8).click(element8).perform()

    # another example

    # action = webdriver.ActionChains(driver).move_to_element(element8)
    # action.perform()

    # ANOTEHR ONE
    # action = action_chains.ActionChains(driver)
    # action.move_to_element(element8)
    # action.click()
    # action.perform()


    # driver.execute_script('arguments[0].click();', element8)



    # except:
    #     driver.refresh()
    #     time.sleep(1)
    #     driver.get('http://patentbusiness.13ij.net/goods/allList.htm#')
    #     # driver.find_element_by_link_text(u"+添加商品").click()
    #     print('gama' + str(i))
    #     i = i - 1
    #     continue
