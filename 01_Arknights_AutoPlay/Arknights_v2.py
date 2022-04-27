# 基于有限状态自动机的明日方舟自动化脚本
# v2.1
# 窗口分辨率=1000*562, DPI=187
# 2022.2.8
# tys

import pyautogui
import time

# 动作之后延迟0.5秒
pyautogui.PAUSE = 0.75
confid = 0.6

def clickLocate(target):
    here = pyautogui.position()
    location = pyautogui.locateCenterOnScreen(target, confidence=confid)
    if location is None:
        return 0
    pyautogui.click(location.x, location.y)
    pyautogui.moveTo(here.x, here.y) # 鼠标回原位
    return 1

class Arknights:
    def __init__(self, loop):
        self.loop = loop
        self.count = 0
        self.img = ['./01_Arknights_AutoPlay/pic/start.png',
            './01_Arknights_AutoPlay/pic/go.png',
            './01_Arknights_AutoPlay/pic/game.png',
            './01_Arknights_AutoPlay/pic/rec.png',
            './01_Arknights_AutoPlay/pic/end.png',
            './01_Arknights_AutoPlay/pic/auto.png']

    # 状态0：关卡选择界面
    def stateStart(self):
        clickLocate(self.img[5]) # 如果代理指挥关闭，则开启
        if clickLocate(self.img[0]):
            print('     ---Start---')
            time.sleep(1)
            return 1
        else:
            return 5

    # 状态1：阵容选择界面
    def stateGo(self):
        if clickLocate(self.img[1]):
            print('     --- Go ---')
            time.sleep(120)
            return 2
        else:
            return 5

    # 状态2：关卡中等待
    def stateGame(self):
        while True:
            if not pyautogui.locateCenterOnScreen(self.img[2], confidence=confid):
                if pyautogui.locateCenterOnScreen(self.img[3], confidence=confid):
                    return 3
                elif pyautogui.locateCenterOnScreen(self.img[4], confidence=confid):
                    return 4
                else:
                    return 5
            else:
                time.sleep(10)    

    # 状态3：保存自动作战
    def stateRec(self):
        if clickLocate(self.img[3]):
            print('     ---Rec---')
            time.sleep(2.5)
            return 4
        else:
            return 5

    # 状态4：作战结束界面
    def stateEnd(self):
        if clickLocate(self.img[4]):
            print('     ---End---')
            self.count += 1
            time.sleep(2)
            return 0
        else:
            return 5

    # 状态5：寻找当前状态
    def stateFind(self):
        for num in range(5):
            if pyautogui.locateCenterOnScreen(self.img[num], confidence=confid):
                print('  we are in state ', num)
                return num
        # 未找到目标，可能是窗口被覆盖，弹窗询问操作
        mission = pyautogui.confirm(text='未找到目标',buttons=['Continue', 'Cancel'])
        if mission == 'Cancel':
            return -1
        else:
            time.sleep(2)
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
                print('-----------Mission Stopped------------')
                break

            if self.count == self.loop:
                print('-----------Mission Finished------------')
                break


#主函数
if __name__ == '__main__':
    # 输入循环次数，-1为一直循环
    while True:
        loop = int(input('select loop number (-1 for NONESTOP):\n'))
        if loop == -1 or loop > 0:
            break
    a = Arknights(loop)
    a.run()
