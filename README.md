# autoUpload13ij
针对智慧专利港湾商家管理后台自动上传图片以及专利信息
需要火狐浏览器，以及火狐浏览器对应的webdriver



大范围使用了Firefox下的插件Katalon Recorder. 能够对浏览器操作进行录制导出为python2代码。建议客制化调试时使用本插件。


主程序为upload_test.py  PatentSpider.py
1先爬取，
2手动筛选申请人、word替换去除摘要符号、excel left right函数析出IPC 清洗，
3再上传
