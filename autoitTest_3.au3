ControlFocus("文件上传","","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("文件上传","","Edit1","F:\CoursesMaterials\Intellectual Property Mana\DATAUPLOAD\load\3.jpg")

Sleep(1000)

ControlClick("文件上传","","Button1")

Sleep(1000)