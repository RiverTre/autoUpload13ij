# autoUpload13ij
针对智慧专利港湾商家管理后台自动上传图片以及专利信息
需要火狐浏览器，以及火狐浏览器对应的webdriver



大范围使用了Firefox下的插件Katalon Recorder. 能够对浏览器操作进行录制导出为python2代码。建议客制化调试时使用本插件。


主程序为upload_test.py  PatentSpider.py
autoit的exe下载安装好，火狐装好，火狐webdriver的zip下载解压好，代码里需要的包装好。
把代码的execute_path改成刚才解压的位置。用autoit打开.au3改成自己存图片的位置，then 重新convert成exe，教程打开autoit的页面可以看到。
上传代码里把autoIt相关的exe地址改成自己的exe存放地址。
各个代码里的用户名密码改成自己的。
上传代码里有一句写了注释，要改成自己的logo对应的数，找到217，改成自己的数字，比如第一个logo就是1第二个就是2第六个就是6。








1先爬取，
2手动筛选申请人、word替换去除摘要符号、excel left() right()函数析出IPC 清洗，
3再上传

autoit的exe文件要根据运行环境电脑上四张图片存储的位置，更改.au3文件里1.jpg等的位置，重新convert。软件包已经上传，教程详见exe以及.au3的描述内网址，即下述网址。代码已经完成，只需修改1.jpg等图片的路径后重新convert
//referred    https://blog.csdn.net/cigo_2018/article/details/83892304
