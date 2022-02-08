import pyautogui

if __name__ == '__main__':
    im = pyautogui.locateCenterOnScreen('D:/03_HUAWEI/Code/01_Arknights_AutoPlay/pic/start.png', confidence=0.9)
    print(im)