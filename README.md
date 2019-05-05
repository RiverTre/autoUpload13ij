# autoUpload13ij
针对智慧专利港湾商家管理后台自动上传图片以及专利信息
需要火狐浏览器，以及火狐浏览器对应的webdriver



大范围使用了Firefox下的插件Katalon Recorder. 能够对浏览器操作进行录制导出为python2代码。建议客制化调试时使用本插件。


主程序为upload_test.py  PatentSpider.py

1先爬取，
2手动筛选申请人、word替换去除摘要符号、excel left() right()函数析出IPC 清洗，
3再上传

autoit的exe文件要根据运行环境电脑上四张图片存储的位置，更改.au3文件里1.jpg等的位置，重新convert。软件包已经上传，教程详见exe以及.au3的描述内网址，即下述网址。代码已经完成，只需修改1.jpg等图片的路径后重新convert
//referred    https://blog.csdn.net/cigo_2018/article/details/83892304
