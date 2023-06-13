import pyautogui

res = pyautogui.locateOnScreen("edit.png")
print(res)
print(pyautogui.center(res))

#pyautogui.write("i love coding", interval=0.25)
