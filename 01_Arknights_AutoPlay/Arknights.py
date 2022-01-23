import pyautogui
import time

#定义鼠标事件
def mouseClick(clickTimes,lOrR,img):
    location=pyautogui.locateCenterOnScreen(img,confidence=0.85)
    print("  Finding ",img)
    if location is not None:
        pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
        print('      **',lOrR,'click **',clickTimes)
        return True
    else:
        print("Not found")
        return False


#任务
def mainWork(flag,loop):
    if flag == -1:
        pyautogui.keyDown('win')
        pyautogui.press('x')
        pyautogui.keyUp('win')
        pyautogui.press('u')
        pyautogui.press('u')
        return
    i = 0
    while True:
        # 点击进入关卡
        img = 'D:/HUAWEI/Python/pic/start.png'
        while True:
            if mouseClick(1,"left",img):
                time.sleep(1)
                break
        # 点击开始行动
        img = 'D:/HUAWEI/Python/pic/go.png'
        while True:
            if mouseClick(1,"left",img):
                time.sleep(1)
                break
        # 等待打完
        print("Waiting...") 
        time.sleep(150)
        # 剿灭需要额外的步骤
        if flag == 1:
            time.sleep(600)
            img = 'D:/HUAWEI/Python/pic/rec.png'
            while True:
                if mouseClick(1,"left",img):
                    time.sleep(2)
                    break
                time.sleep(60)
        # 行动结束结算页面
        img = 'D:/HUAWEI/Python/pic/end.png'
        while True:
            if mouseClick(1,"left",img):
                time.sleep(2)
                break
            time.sleep(20)
        # 判断循环是否继续
        i += 1
        if i == loop:
            break
    return


#主函数
if __name__ == '__main__':
    # 选择功能：普通or剿灭
    while True:
        key = input('Welcome to Arknights AutoPlay, please select function:\n1.short 2.long\n')
        flag = int(key)-1
        if flag == 1 or flag == 0:
            break
    # 输入循环次数，-1为一直循环
    while True:
        loop = int(input('Please select loop number: (-1:nonstop)\n'))
        if loop == -1 or loop > 0:
            break
    # 完成后是否要关机
    while True:
        end = input('Do you want to shut down after finished? Y/N\n')
        if end == 'Y' or end == 'N':
            break
    
    mainWork(flag,loop)
    print('-----------Mission accomplished------------')
    if end == 'Y':
        mainWork(-1, 1)
