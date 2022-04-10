from time import sleep
import pyautogui

pyautogui.PAUSE =0.75
confid = 0.95
num = 1

while True:
    while True:
        if pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/now.png',confidence=confid):
            break
    print(num)

    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/now.png',confidence=confid))
    
    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/yes.png',confidence=confid))

    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/accept.png',confidence=confid))

    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/skip.png',confidence=0.8))
    sleep(2)
    pyautogui.click()
    num = num + 1
    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/new.png',confidence=confid))

    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            './01_Arknights_AutoPlay/pic2/down.png',confidence=confid))

    if pyautogui.locateCenterOnScreen(
        './01_Arknights_AutoPlay/pic2/ksfh.png',confidence=confid):
        print("ksfh")

    if pyautogui.locateCenterOnScreen(
        './01_Arknights_AutoPlay/pic2/tzgy.png',confidence=confid):
        print("tzgy")

    if pyautogui.locateCenterOnScreen(
        './01_Arknights_AutoPlay/pic2/wy.png',confidence=confid):
        print("wy")