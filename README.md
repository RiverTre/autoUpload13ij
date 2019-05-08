# autoUpload13ij
针对智慧专利港湾商家管理后台自动上传图片以及专利信息

需要火狐浏览器，以及火狐浏览器对应的webdriver

关于配置python环境，方法之一是
1 登录python官网，下载python解释器解压,选最新的3.7就可以
https://www.python.org/downloads/windows/
可以用anaconda替代python解释器，anaconda包含它
2 then搜索Pycharm,下载该IDE使用
https://www.jetbrains.com/pycharm/download/#section=windows//免费版就能用，付费版可以用教育邮箱申请license


大范围使用了Firefox下的插件Katalon Recorder. 能够对浏览器操作进行录制导出为python2代码。建议客制化调试时使用本插件。


主程序为upload.py  PatentSpider.py  ShenHe.py TianJiaRuKu.py(添加入库)  TiJiaoZuHe.py（提交组合）  ShenHeZuHe.py(审核组合) ShangJia.py(点击上架)
若有bug,欢迎一起完善。ShangJia.py基本没问题，因为不给我发验证码短信了，暂时没法调试






PatentSpider.py里把电子科技大学都改成自己的大学名
autoit的exe下载安装好，火狐装好，火狐webdriver的zip下载解压好，代码里需要的包装好。
（每个）代码的execute_path改成刚才解压的位置。用autoit打开.au3改成自己存图片的位置，then 重新convert成exe，教程打开autoit的页面可以看到。
上传代码里把autoIt相关的exe地址改成自己的exe存放地址。
各个代码里的用户名密码改成自己的。
上传代码里有一句写了注释，要改成自己的logo对应的数，找到217，改成自己的数字，比如第一个logo就是1第二个就是2第六个就是6。
数据清洗用到left()right()两个公式。注意把公式结果在原位置复制粘贴成值。注意最后要把没有数据的行删除一遍，CTRL+shift＋↓向下选择全部。
摘要有奇怪字符，left(),数值参数为一百，例如=left(D1,100)。把摘要粘到word，带格式粘贴，处理完带格式粘贴回来，教程http://www.exceltip.net/thread-54253-1-1.html。
按照项目的样例对照自己处理的正误。





1先爬取，
2手动筛选申请人、word替换去除摘要符号、excel left() right()函数析出IPC 清洗，
3再上传

autoit的exe文件要根据运行环境电脑上四张图片存储的位置，更改.au3文件里1.jpg等的位置，重新convert。软件包已经上传，教程详见exe以及.au3的描述内网址，即下述网址。代码已经完成，只需修改1.jpg等图片的路径后重新convert
//referred    https://blog.csdn.net/cigo_2018/article/details/83892304


