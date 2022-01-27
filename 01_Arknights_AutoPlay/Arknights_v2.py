# 带自动纠偏机制的基于有限状态自动机明日方舟脚本

import pyautogui
import time
# 动作之后延迟0.5秒
pyautogui.PAUSE = 0.75
conf = 0.75

class Arknights:
    def __init__(self, loop):
        self.loop = loop
        self.count = 0
        self.img = ['D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/start.png',
            'D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/go.png',
            'D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/game.png',
            'D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/rec.png',
            'D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/end.png',
            'D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/auto.png']

    # 状态0：关卡选择界面
    def stateStart(self):
        location=pyautogui.locateCenterOnScreen(self.img[0], confidence=conf)
        if location is None:
            return 5
        # 如果代理指挥关闭，则开启
        auto=pyautogui.locateCenterOnScreen(self.img[5], confidence=conf)
        if auto is not None:
            pyautogui.click(auto.x, auto.y, duration=0.2)
        pyautogui.click(location.x, location.y, duration=0.2)
        print('     ---Start---')
        time.sleep(1.5)
        return 1

    # 状态1：阵容选择界面
    def stateGo(self):
        location=pyautogui.locateCenterOnScreen(self.img[1], confidence=conf)
        if location is None:
            return 5
        pyautogui.click(location.x, location.y, duration=0.2)
        print('     ---Go---')
        time.sleep(120)
        return 2

    # 状态2：关卡中等待
    def stateGame(self):
        while True:
            location1=pyautogui.locateCenterOnScreen(self.img[2], confidence=conf)
            time.sleep(2)
            location2=pyautogui.locateCenterOnScreen(self.img[2], confidence=conf)
            if location1 is None and location2 is None:
                if pyautogui.locateCenterOnScreen(self.img[3], confidence=conf) is not None:
                    return 3
                elif pyautogui.locateCenterOnScreen(self.img[4], confidence=conf) is not None:
                    return 4
                else:
                    return 5
            else:
                time.sleep(10)    

    # 状态3：保存自动作战
    def stateRec(self):
        location=pyautogui.locateCenterOnScreen(self.img[3], confidence=conf)
        if location is None:
            return 5
        pyautogui.click(location.x, location.y, duration=0.2)
        print('     ---Rec---')
        time.sleep(2.5)
        return 4

    # 状态4：作战结束界面
    def stateEnd(self):
        location=pyautogui.locateCenterOnScreen(self.img[4],confidence=conf)
        if location is None:
            return 5
        pyautogui.click(location.x,location.y,duration=0.2)
        print('     ---End---')
        self.count += 1
        time.sleep(2.5)
        return 0

    # 状态5：寻找当前状态
    def stateFind(self):
        num = 0
        for target in self.img:
            location=pyautogui.locateCenterOnScreen(target, confidence=conf)
            if location is not None:
                print('  ** we are in state ', num)
                return num
            num += 1
        # 未找到目标，可能是窗口被覆盖，弹窗询问操作
        mission = pyautogui.confirm(text='未找到目标', title='Arknight Autogui', buttons=['Continue', 'Cancel'])
        if mission == 'Cancel':
            return -1
        else:
            time.sleep(1)
            return 5

    # 主循环
    def run(self):
        state = self.stateFind()
        while True:
            if state == 0:
                state = self.stateStart()
            elif state == 1:
                state = self.stateGo()
            elif state == 2:
                state = self.stateGame()
            elif state == 3:
                state = self.stateRec()
            elif state == 4:
                state = self.stateEnd()
            elif state == 5:
                state = self.stateFind()
            else: # 当返回-1时，程序结束
                break

            if self.count == self.loop:
                break

#主函数
if __name__ == '__main__':
    # 输入循环次数，-1为一直循环
    while True:
        loop = int(input('Please select loop number: (-1:nonstop)\n'))
        if loop == -1 or loop > 0:
            break
    a = Arknights(loop)
    a.run()
    print('-----------Mission accomplished------------')

