import time
import pyautogui

pyautogui.click(1260, 1560)  # Switch to BlueStacks!
print("Bluestaacks is now selected.")
while True:
    pyautogui.click(1260, 1560)  # Attack!
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(2153, 1371)  # Find a Match
    time.sleep(5)  # Wait for 5 second
    for i in range(5):
        pyautogui.keyDown('down') # Zoom out
    pyautogui.keyUp('down')  # Release the down key
    pyautogui.click(1315, 1575)  # Dragon!
    for i in range(17): 
        pyautogui.click(2366, 1263)  # Deploy Dragons at right corner!
    pyautogui.click(1544, 1575)  # Hero 1 Selection!
    pyautogui.click(2366, 1263)  # Deploy Hero 1 at right corner!
    pyautogui.click(1656, 1575)  # Hero 2 Selection!
    pyautogui.click(2366, 1263)  # Deploy Hero 2 at right corner!
    pyautogui.click(1748, 1575)  # Hero 3 Selection!
    pyautogui.click(2366, 1263)  # Deploy Hero 3 at right corner!
    pyautogui.click(1845, 1575)  # Hero 4 Selection!
    pyautogui.click(2366, 1263)  # Deploy Hero 4 at right corner!
    pyautogui.click(1544, 1575)  # Activate Hero 1 ability!
    pyautogui.click(1656, 1575)  # Activate Hero 2 ability!
    pyautogui.click(1748, 1575)  # Activate Hero 3 ability!
    pyautogui.click(1845, 1575)  # Activate Hero 4 ability!
    time.sleep(87)  # Wait for 87 seconds
    pyautogui.click(1277, 1461)  # Surrender
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(1998, 1383)  # Okay
    time.sleep(2)  # Wait for 2 second
    pyautogui.click(1850, 1547)  # Return Home!
    time.sleep(5)  # Wait for 5 seconds
    pyautogui.click(1652, 1152)  # Address Errors!
    time.sleep(9)  # Wait for 9 seconds