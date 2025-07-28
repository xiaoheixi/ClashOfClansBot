import time
import pyautogui

while True:
    pyautogui.click(1368, 1349)  # Attack!
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(2175, 1134)  # Find a Match
    time.sleep(5)  # Wait for 5 second
    for i in range(5):
        pyautogui.keyDown('down') # Zoom out
    pyautogui.keyUp('down')  # Release the down key
    pyautogui.click(1619, 1363)  # Hero 1 Selection!
    pyautogui.click(2403, 1063)  # Deploy Hero 1 at right corner!
    pyautogui.click(1714, 1365)  # Hero 2 Selection!
    pyautogui.click(2403, 1063)  # Deploy Hero 2 at right corner!
    pyautogui.click(1796, 1357)  # Hero 3 Selection!
    pyautogui.click(2403, 1063)  # Deploy Hero 3 at right corner!
    pyautogui.click(1896, 1363)  # Hero 4 Selection!
    pyautogui.click(2403, 1063)  # Deploy Hero 4 at right corner!
    pyautogui.click(1619, 1363)  # Activate Hero 1 ability!
    pyautogui.click(1714, 1365)  # Activate Hero 2 ability!
    pyautogui.click(1796, 1357)  # Activate Hero 3 ability!
    pyautogui.click(1896, 1363)  # Activate Hero 4 ability!
    time.sleep(50)  # Wait for 50 seconds
    pyautogui.click(1371, 1263)  # Surrender
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(2044, 1190)  # Okay
    time.sleep(2)  # Wait for 2 second
    pyautogui.click(1906, 1336)  # Return Home!
    time.sleep(5)  # Wait for 5 seconds
    pyautogui.click(1652, 1152)  # Address Errors!
    time.sleep(9)  # Wait for 9 seconds