import pyautogui
import time
import xlrd
import pyperclip

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

#定义鼠标事件
def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry > 0:
        for i in range(0, reTry):
            while 1:
                location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
                if location is not None:
                    pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                    print(lOrR,'*',clickTimes)
                    break
                print("not found, retry after 1s")
                time.sleep(1)
    else:
        print("clicking~~~")
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(1)


# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(sheet):
    checkCmd = True
    print(sheet.row(0)[1])
    #行数检查
    if sheet.nrows<2:
        print("no data")
        checkCmd = False
    #每行数据检查
    i = 1
    while i < sheet.nrows:
        # 第1列 操作类型检查
        cmdType = sheet.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0 
        and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0):
            print('line ', i+1,", row 1 data error")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = sheet.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value ==1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('line ', i+1,", row 2 data error")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('line ',i+1,", row 2 data error")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('line ',i+1,", row 2 data error")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('line ',i+1,", row 2 data error")
                checkCmd = False
        i += 1
    return checkCmd


#任务
def mainWork(sheet):
    i = 1
    while i < sheet.nrows:
        #取本行指令的操作类型
        cmdType = sheet.row(i)[0]
        #1 2 3代表鼠标点击操作
        if cmdType.value == 1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            #取图片名称
            img = sheet.row(i)[1].value
            print("finding ",img)
            #取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = int(sheet.row(i)[2].value)
            #1单机左键
            if cmdType.value == 1.0:
                mouseClick(1,"left",img,reTry)
            #2双击左键
            elif cmdType.value == 2.0:
                mouseClick(2,"left",img,reTry)
            #3代表右键
            else:
                mouseClick(1,"right",img,reTry)
        #4代表输入
        elif cmdType.value == 4.0:
            #取输入内容
            inputValue = sheet.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("type: ",inputValue)                                        
        #5代表等待
        elif cmdType.value == 5.0:
            #取等待时间
            waitTime = sheet.row(i)[1].value
            time.sleep(waitTime)
            print("wait ",waitTime," s")
        #6代表滚轮
        elif cmdType.value == 6.0:
            #取滚动距离
            scroll = sheet.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("scroll",int(scroll))                      
        i += 1

#主函数
if __name__ == '__main__':
    file = "D:/HUAWEI/Python/Autogui.xls"
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    if wb is None:
        print("no such file or directory")
    key=input('Welcome, please input sheet number: \n')
    num=int(key)-1
    #通过索引获取表格sheet页
    sheet = wb.sheet_by_index(num)
    #数据检查
    checkCmd = dataCheck(sheet)
    if checkCmd:
        key=input('choose function: 1.once 2.loop \n')
        if key=='1':
            #循环拿出每一行指令
            mainWork(sheet)
        elif key=='2':
            while True:
                mainWork(sheet)
                time.sleep(1)
    else:
        print('data error, exiting')
