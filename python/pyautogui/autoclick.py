import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

# CLICK 1
pyautogui.moveTo(30, 30) 
pyautogui.click()   

# CLICK 2
pyautogui.moveTo(1650, 1080, duration=5, tween=pyautogui.easeInOutQuad)
pyautogui.click() 

# CLICK 3
pyautogui.moveTo(270, 1080, duration=5, tween=pyautogui.easeInOutQuad)
pyautogui.click()

# CLICK 4
pyautogui.moveTo(820, 970, duration=5, tween=pyautogui.easeInOutQuad)
pyautogui.click()



# pyautogui.move(0, 10)
# pyautogui.doubleClick()
# pyautogui.click('button.png')


